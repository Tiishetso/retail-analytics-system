from config.config import get_db_config
from etl.extract import extract_data
from etl.transform import transform_data
from etl.load import create_mysql_engine, load_to_mysql
from etl.data_quality import (
    missing_value_report,
    validate_schema,
    detect_anomalies,
    data_quality_score
)


def run_pipeline(file_path):
    print("ETL PIPELINE STARTED")

    # -------------------------
    # 1. EXTRACT
    # -------------------------
    df = extract_data(file_path)

    if df is None:
        print("Pipeline stopped at extract stage")
        return

    # -------------------------
    # 2. TRANSFORM
    # -------------------------
    df = transform_data(df)

    # -------------------------
    # 3. DATA QUALITY LAYER
    # -------------------------
    print("\nDATA QUALITY CHECKS\n")

    required_columns = [
        "store",
        "date",
        "weekly_sales",
        "temperature",
        "fuel_price",
        "cpi",
        "unemployment"
    ]

    # Missing values report
    missing_report = missing_value_report(df)
    print("Missing Values (%):")
    print(missing_report)

    # Schema validation
    try:
        validate_schema(df, required_columns)
        print("Schema validation passed")
    except Exception as e:
        print(f"Schema validation failed: {e}")
        return

    # Anomaly detection
    anomalies = detect_anomalies(df, "weekly_sales")
    if anomalies is not None:
        print(f"Anomalies detected: {len(anomalies)} rows")

    # Data quality score
    score = data_quality_score(df, required_columns)
    print(f"Data Quality Score: {score}/100")

    if score < 60:
        print("Data quality too low - stopping pipeline")
        return

    # -------------------------
    # 4. LOAD
    # -------------------------
    config = get_db_config()
    engine = create_mysql_engine(config)

    if engine is None:
        print("Failed to create MySQL engine")
        return

    load_to_mysql(df, engine)

    print("ETL PIPELINE COMPLETED")