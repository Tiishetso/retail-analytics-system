import pandas as pd


# -----------------------------
# 1. Missing Value Report
# -----------------------------
def missing_value_report(df: pd.DataFrame):
    """
    Returns missing value percentage per column
    """
    report = (df.isnull().sum() / len(df)) * 100
    return report.sort_values(ascending=False)


# -----------------------------
# 2. Schema Validation
# -----------------------------
def validate_schema(df: pd.DataFrame, required_columns: list):
    """
    Ensures required columns exist in dataset
    """

    missing_cols = [col for col in required_columns if col not in df.columns]

    if missing_cols:
        raise Exception(f"Missing required columns: {missing_cols}")

    return True


# -----------------------------
# 3. Anomaly Detection (IQR)
# -----------------------------
def detect_anomalies(df: pd.DataFrame, column: str):
    """
    Detect outliers using IQR method
    """

    if column not in df.columns:
        return None

    Q1 = df[column].quantile(0.25)
    Q3 = df[column].quantile(0.75)

    IQR = Q3 - Q1

    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR

    anomalies = df[(df[column] < lower_bound) | (df[column] > upper_bound)]

    return anomalies


# -----------------------------
# 4. Data Quality Score (NEW)
# -----------------------------
def data_quality_score(df: pd.DataFrame, required_columns: list):
    """
    Returns a score out of 100 based on:
    - Missing values
    - Schema completeness
    """

    score = 100

    # Missing values penalty
    missing_pct = (df.isnull().sum().sum() / (len(df) * len(df.columns))) * 100
    score -= missing_pct * 0.5  # weighted penalty

    # Schema penalty
    missing_cols = [col for col in required_columns if col not in df.columns]
    score -= len(missing_cols) * 10

    # Clamp score
    if score < 0:
        score = 0

    return round(score, 2)