import mysql.connector
from functools import wraps

def with_db_connection():
    """
    Decorator that opens a database connection, passes it to the decorated function,
    and ensures the connection is closed after execution.
    """
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            connection = mysql.connector.connect(
                host="localhost",
                user="Nebula",
                password="Nebula@20",
                database="ALX_prodev"
            )
            try:
                # Pass the connection as a keyword argument
                return func(*args, connection=connection, **kwargs)
            finally:
                connection.close()
        return wrapper
    return decorator