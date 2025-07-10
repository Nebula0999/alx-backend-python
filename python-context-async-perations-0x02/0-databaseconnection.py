import mysql.connector

class DatabaseConnection:
    """
    Context manager to handle opening and closing database connections automatically.
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

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.cursor:
            self.cursor.close()
        if self.connection:
            if exc_type:
                self.connection.rollback()
            else:
                self.connection.commit()
            self.connection.close()


# Example usage with `with` and `SELECT * FROM users`
if __name__ == "__main__":
    with DatabaseConnection(
        host="localhost",
        user="Nebula",
        password="Nebula@20",
        database="ALX_prodev"
    ) as cursor:
        cursor.execute("SELECT * FROM users")  # <-- SELECT * FROM users
        results = cursor.fetchall()
        for row in results:
            print(row)
