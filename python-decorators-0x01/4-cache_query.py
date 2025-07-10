from functools import wraps

# In-memory cache dictionary
query_cache = {}

def cache_query(func):
    """
    Decorator that caches the result of a SQL query based on the query string.
    """
    @wraps(func)
    def wrapper(query, *args, **kwargs):
        if query in query_cache:
            print("[CACHE] Returning cached result for query.")
            return query_cache[query]

        # Run the actual query function
        result = func(query, *args, **kwargs)
        query_cache[query] = result
        return result
    return wrapper