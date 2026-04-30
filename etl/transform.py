import pandas as pd


def transform_data(df):
    try:
        df = df.copy()

        # -------------------------
        # CLEAN COLUMN NAMES
        # -------------------------
        df.columns = df.columns.str.lower().str.replace(" ", "_")

        # -------------------------
        # REMOVE DUPLICATES
        # -------------------------
        df = df.drop_duplicates()

        # -------------------------
        # DATE FIX (your format)
        # -------------------------
        if "date" in df.columns:
            df["date"] = pd.to_datetime(
                df["date"],
                format="%d-%m-%Y",
                errors="coerce"
            )

        # -------------------------
        # TYPE CONVERSION
        # -------------------------
        numeric_cols = [
            "store",
            "weekly_sales",
            "temperature",
            "fuel_price",
            "cpi",
            "unemployment",
            "holiday_flag"
        ]

        for col in numeric_cols:
            if col in df.columns:
                df[col] = pd.to_numeric(df[col], errors="coerce")

        # -------------------------
        # FEATURE ENGINEERING 
        # -------------------------

        if "fuel_price" in df.columns:
            df["high_fuel"] = df["fuel_price"] > df["fuel_price"].mean()

        if "cpi" in df.columns:
            df["high_cpi"] = df["cpi"] > df["cpi"].mean()

        if "unemployment" in df.columns:
            df["high_unemployment"] = df["unemployment"] > df["unemployment"].mean()

        print("feature engineering completed")

        return df

    except Exception as e:
        print(f"Transform error: {e}")
        return df