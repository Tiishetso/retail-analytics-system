import pandas as pd
from utils.logger import setup_logger

logger = setup_logger("extract_logger")


def extract_data(file_path: str):
    try:
        df = pd.read_csv(file_path)

        if df.empty:
            logger.warning("Dataset is empty")
            return None

        logger.info("Data loaded successfully")
        logger.info(f"Rows: {len(df)}")
        logger.info(f"Columns: {len(df.columns)}")

        return df

    except FileNotFoundError:
        logger.error(f"File not found: {file_path}")
        return None

    except pd.errors.EmptyDataError:
        logger.error("CSV file is empty or invalid")
        return None

    except Exception as e:
        logger.exception(f"Unexpected error during extract: {e}")
        return None