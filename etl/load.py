from utils.logger import setup_logger
from sqlalchemy import create_engine

logger = setup_logger("load_logger")


def create_mysql_engine(config):
    try:
        engine = create_engine(
            f"mysql+pymysql://{config['user']}:{config['password']}"
            f"@{config['host']}:{config['port']}/{config['database']}"
        )

        logger.info("MySQL engine created successfully")
        return engine

    except Exception as e:
        logger.exception(f"Engine creation failed: {e}")
        return None


def load_to_mysql(df, engine, table_name="walmart_sales"):
    try:
        df.to_sql(
            name=table_name,
            con=engine,
            if_exists="replace",
            index=False
        )

        logger.info(f"Data loaded into table: {table_name}")

    except Exception as e:
        logger.exception(f"Load failed: {e}")