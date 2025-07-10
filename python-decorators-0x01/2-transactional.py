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
                user="your_mysql_user",
                password="your_mysql_password",
                database="ALX_prodev"
            )
            try:
                return func(*args, connection=connection, **kwargs)
            finally:
                connection.close()
        return wrapper
    return decorator


def transactional(func):
    """
    Decorator that manages transactions: commits on success, rollbacks on failure.
    Requires a 'connection' keyword argument.
    """
    @wraps(func)
    def wrapper(*args, **kwargs):
        connection = kwargs.get('connection')
        if connection is None:
            raise ValueError("A 'connection' keyword argument is required for transactional operations.")

        try:
            result = func(*args, **kwargs)
            connection.commit()
            print("[TRANSACTION] Committed successfully.")
            return result
        except Exception as e:
            connection.rollback()
            print(f"[TRANSACTION] Rolled back due to error: {e}")
            raise
    return wrapper
