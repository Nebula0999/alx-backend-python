from datetime import datetime
from functools import wraps
import mysql.connector

def connect():
    """
    Connects to the MySQL database and returns a connection object.
    """
    return mysql.connector.connect(
        host="localhost",
        user="Nebula",
        password="Nebula@20",
        database="ALX_prodev"
    )

def log_queries():
    """
    Decorator that logs SQL queries with timestamps before executing them.
    Assumes the first argument is the SQL query string.
    """
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            if args:
                query = args[0]
                print(f"[{datetime.now()}] Executing SQL: {query}")
            return func(*args, **kwargs)
        return wrapper
    return decorator
