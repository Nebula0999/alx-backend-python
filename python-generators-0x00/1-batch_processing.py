import mysql.connector

def stream_users_in_batches(batch_size):
    """
    Generator that yields rows from user_data in batches.
    """
    connection = mysql.connector.connect(
        host="localhost",
        user="your_mysql_user",
        password="your_mysql_password",
        database="ALX_prodev"
    )
    cursor = connection.cursor(dictionary=True)

    try:
        cursor.execute("SELECT * FROM user_data")
        while True:
            batch = cursor.fetchmany(batch_size)
            if not batch:
                break
            yield batch
    finally:
        cursor.close()
        connection.close()


def batch_processing(batch_size):
    """
    Generator that yields only users over age 25 from batches.
    """
    for batch in stream_users_in_batches(batch_size):  # 1st loop
        filtered = [user for user in batch if user['age'] > 25]  # 2nd loop
        for user in filtered:  # 3rd loop
            yield user

    return 


if __name__ == "__main__":
    for user in batch_processing(batch_size=3):
        print(user)
