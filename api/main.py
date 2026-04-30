# api/main.py

from fastapi import FastAPI
from sqlalchemy.orm import sessionmaker
from sqlalchemy import text
from utils.logger import setup_logger
from etl.load import create_mysql_engine
from config.config import get_db_config

# Setup logger
logger = setup_logger("api_logger")

# Initialize FastAPI app
app = FastAPI(title="Weather Analytics API")

# Create SQLAlchemy engine using your reusable function
engine = create_mysql_engine(get_db_config())
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


# --- SALES ENDPOINTS ---
@app.get("/sales/holiday")
def get_holiday_sales():
    try:
        with engine.connect() as conn:
            result = conn.execute(text("SELECT * FROM holiday_sales")).fetchall()
            logger.info("Holiday sales data retrieved successfully")
            return [dict(row._mapping) for row in result]
    except Exception as e:
        logger.exception(f"Failed to fetch holiday sales: {e}")
        return {"error": "Could not fetch holiday sales"}


@app.get("/sales/monthly")
def get_monthly_sales():
    try:
        with engine.connect() as conn:
            result = conn.execute(text("SELECT * FROM monthly_sales")).fetchall()
            logger.info("Monthly sales data retrieved successfully")
            return [dict(row._mapping) for row in result]
    except Exception as e:
        logger.exception(f"Failed to fetch monthly sales: {e}")
        return {"error": "Could not fetch monthly sales"}


# --- PERFORMANCE ENDPOINTS ---
@app.get("/performance/stores")
def get_store_performance():
    try:
        with engine.connect() as conn:
            result = conn.execute(text("SELECT * FROM store_performance")).fetchall()
            logger.info("Store performance data retrieved successfully")
            return [dict(row._mapping) for row in result]
    except Exception as e:
        logger.exception(f"Failed to fetch store performance: {e}")
        return {"error": "Could not fetch store performance"}


# --- ECONOMIC ENDPOINTS ---
@app.get("/economic/sensitivity")
def get_economic_sensitivity():
    try:
        with engine.connect() as conn:
            result = conn.execute(text("SELECT * FROM economic_sensitivity")).fetchall()
            logger.info("Economic sensitivity data retrieved successfully")
            return [dict(row._mapping) for row in result]
    except Exception as e:
        logger.exception(f"Failed to fetch economic sensitivity: {e}")
        return {"error": "Could not fetch economic sensitivity"}


@app.get("/economic/stress-index")
def get_stress_index():
    try:
        with engine.connect() as conn:
            result = conn.execute(text("SELECT * FROM stress_index_view")).fetchall()
            logger.info("Stress index data retrieved successfully")
            return [dict(row._mapping) for row in result]
    except Exception as e:
        logger.exception(f"Failed to fetch stress index: {e}")
        return {"error": "Could not fetch stress index"}


@app.get("/economic/factors")
def get_sales_economic_factors():
    try:
        with engine.connect() as conn:
            result = conn.execute(text("SELECT * FROM sales_economic_factors_view")).fetchall()
            logger.info("Sales economic factors data retrieved successfully")
            return [dict(row._mapping) for row in result]
    except Exception as e:
        logger.exception(f"Failed to fetch sales economic factors: {e}")
        return {"error": "Could not fetch sales economic factors"}


# --- WEATHER ENDPOINTS ---
@app.get("/weather/sales-with-temp")
def get_sales_with_temperature():
    try:
        with engine.connect() as conn:
            result = conn.execute(text("SELECT * FROM sales_with_temperature")).fetchall()
            logger.info("Sales with temperature data retrieved successfully")
            return [dict(row._mapping) for row in result]
    except Exception as e:
        logger.exception(f"Failed to fetch sales with temperature: {e}")
        return {"error": "Could not fetch sales with temperature"}


@app.get("/weather/sales-temp")
def get_sales_temperature():
    try:
        with engine.connect() as conn:
            result = conn.execute(text("SELECT * FROM sales_temperature_view")).fetchall()
            logger.info("Sales temperature data retrieved successfully")
            return [dict(row._mapping) for row in result]
    except Exception as e:
        logger.exception(f"Failed to fetch sales temperature: {e}")
        return {"error": "Could not fetch sales temperature"}
