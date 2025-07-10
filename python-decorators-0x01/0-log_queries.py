from functools import wraps

def log_queries():
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            if args:
                query = args[0]  # Assumes first argument is the SQL query string
                print(f"[QUERY LOG] Executing SQL: {query}")
            return func(*args, **kwargs)
        return wrapper
    return decorator