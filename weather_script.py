import pandas as pd
from sqlalchemy import create_engine
from dotenv import load_dotenv
import os

load_dotenv()

#%%
# Load dataset
def load_data(file_path):
    try:
        data = pd.read_csv(file_path)
        print("Data loaded successfully.")
        return data
    except Exception as e:
        print(f"Error loading data: {e}")
        return None

df = load_data("walmart_sales.csv")

print(df.head(10))

print(len(df))

#%%
# Cleaning column names 
# def clean_data(df):
#     try:
#         df.columns = df.columns.str.lower().str.replace(" ", "_")

#         df = df.drop_duplicates()

#         #Converting data types & creating new features

#         if "date" in df.columns:
#             df["date"] = pd.to_datetime(df["date"], format="%d-%m-%Y", errors="coerce")

#         if "holiday_flag" in df.columns:
#             df["holiday_flag"] = df["holiday_flag"].astype(int)

#         if "temperature" in df.columns:
#             df["temperature"] = pd.to_numeric(df["temperature"], errors="coerce")

#         if "fuel_price" in df.columns:
#             df["fuel_price"] = pd.to_numeric(df["fuel_price"], errors="coerce")
#             df['high_fuel'] = df['fuel_price'] > df['fuel_price'].mean()

#         if "cpi" in df.columns:
#             df["cpi"] = pd.to_numeric(df["cpi"], errors="coerce")
#             df['high_cpi'] = df['cpi'] > df['cpi'].mean()

#         if "unemployment" in df.columns:
#             df["unemployment"] = pd.to_numeric(df["unemployment"], errors="coerce")
#             df['high_unemployment'] = df['unemployment'] > df['unemployment'].mean()

#         if "weekly_sales" in df.columns:
#             df["weekly_sales"] = pd.to_numeric(df["weekly_sales"], errors="coerce")

#         if "store" in df.columns:
#             df["store"] = df["store"].astype(int)

#         print("Data cleaning completed successfully.")
#         return df
#     except Exception as e:
#         print(f"Error cleaning data: {e}")
#         return df

    
# df = clean_data(df)
# #%%
# # MySQL connection


def get_db_config():
    try:
        return {
            "user": os.environ["user"],
            "password": os.environ["password"],
            "host": os.environ["host"],
            "port": int(os.environ["port"]),
            "database": os.environ["database"]
        }
    except KeyError as e:
        raise Exception(f"Missing environment variable: {e}")
    

def create_mysql_engine(user, password, host, port, database):
    try:
        engine = create_engine(f"mysql+pymysql://{user}:{password}@{host}:{port}/{database}")
        print("MySQL engine created successfully.")
        return engine
    except Exception as e:
        print(f"Error creating MySQL engine: {e}")
        return None

config = get_db_config()

engine = create_mysql_engine(
    user=config["user"],
    password=config["password"],
    host=config["host"],
    port=config["port"],
    database=config["database"]
)


# Push to MySQL
def push_to_mysql(df, engine):
    try:
        df.to_sql(
            name="walmart_sales",
            con=engine,
            if_exists="replace",  
            index=False
        )
        print("Data pushed to MySQL successfully.")
    except Exception as e:
        print(f"Error pushing data to MySQL: {e}")

push_to_mysql(df, engine)


