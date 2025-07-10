import mysql.connector

class DatabaseConnection:
    """
    Custom context manager to handle opening and closing MySQL database connections.
    """

    def __init__(self, host, user, password, database):
        self.config = {
            'host': host,
            'user': user,
            'password': password,
            'database': database
        }
        self.connection = None
        self.cursor = None

    def __enter__(self):
        self.connection = mysql.connector.connect(**self.config)
        self.cursor = self.connection.cursor(dictionary=True)
        return self.cursor

    def __exit__(self, exc_type, exc_value, traceback):
        if self.cursor:
            self.cursor.close()
        if self.connection:
            if exc_type is not None:
                self.connection.rollback()  # Optional: rollback on error
            else:
                self.connection.commit()
            self.connection.close()