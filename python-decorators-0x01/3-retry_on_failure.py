import time
from functools import wraps
import mysql.connector

def retry_on_failure(retries=3, delay=2):
    """
    Decorator that retries the decorated function if it raises an exception.
    :param retries: Number of retry attempts
    :param delay: Seconds to wait between retries
    """
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            last_exception = None
            for attempt in range(1, retries + 1):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    last_exception = e
                    print(f"[RETRY {attempt}/{retries}] Error: {e}")
                    if attempt < retries:
                        time.sleep(delay)
            print("[RETRY] Operation failed after all retries.")
            raise last_exception
        return wrapper
    return decorator