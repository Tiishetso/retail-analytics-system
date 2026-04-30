from dotenv import load_dotenv
import os

# Load .env file once when config module is imported
load_dotenv()


class ConfigError(Exception):
    """Custom exception for configuration-related issues"""
    pass


def get_env_variable(name: str):
    """
    Safely fetch environment variables.
    Raises a clear error if missing.
    """
    value = os.getenv(name)

    if value is None or value.strip() == "":
        raise ConfigError(f"Missing required environment variable: {name}")

    return value


def get_db_config():
    """
    Returns validated database configuration from .env
    """

    try:
        user = get_env_variable("user")
        password = get_env_variable("password")
        host = get_env_variable("host")
        port = get_env_variable("port")
        database = get_env_variable("database")

        return {
            "user": user,
            "password": password,
            "host": host,
            "port": int(port),
            "database": database
        }

    except ValueError as ve:
        raise ConfigError(f"Invalid numeric value in config (port issue): {ve}")

    except Exception as e:
        raise ConfigError(f"Error loading database config: {e}")