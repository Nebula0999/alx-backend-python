import mysql.connector

def stream_users():
    """
    Generator that yields user_data rows one by one from the MySQL database.
    """
    connection = mysql.connector.connect(
        host="localhost",
        user="Nebula",
        password="Nebula@2025",
        database="ALX_prodev"
    )
    cursor = connection.cursor(dictionary=True)

    try:
        cursor.execute("SELECT * FROM user_data")

        for row in cursor:
            yield row

    finally:
        cursor.close()
        connection.close()

if __name__ == "__main__":
    for user in stream_users():
        print(user)
