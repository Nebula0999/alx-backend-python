import mysql.connector
from mysql.connector import errorcode
import pandas as pd
import uuid


def connect_db():
    return mysql.connector.connect(
        host="localhost",
        user="Nebula",
        password="Nebula@2025",
    )

def create_database(connection):
    cursor = connection.cursor()
    try:
        cursor.execute("CREATE DATABASE IF NOT EXISTS ALX_prodev")
        print("[✔] Database ALX_prodev ensured.")
    except mysql.connector.Error as err:
        print(f"[✖] Error creating database: {err}")
    finally:
        cursor.close()

def connect_to_prodev():
    return mysql.connector.connect(
        host="localhost",
        user="your_mysql_user",
        password="your_mysql_password",
        database="ALX_prodev"
    )

def create_table(connection):
    cursor = connection.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS user_data (
            user_id VARCHAR(36) PRIMARY KEY,
            name VARCHAR(255) NOT NULL,
            email VARCHAR(255) NOT NULL,
            age DECIMAL(3,0) NOT NULL,
            UNIQUE(email),
            INDEX(user_id)
        );
    """)
    print("[✔] Table user_data ensured.")
    cursor.close()

def insert_data(connection, data):
    cursor = connection.cursor()
    inserted = 0
    for _, row in data.iterrows():
        try:
            user_id = str(uuid.uuid4())
            cursor.execute("""
                INSERT IGNORE INTO user_data (user_id, name, email, age)
                VALUES (%s, %s, %s, %s)
            """, (user_id, row['name'], row['email'], row['age']))
            inserted += cursor.rowcount
        except mysql.connector.Error as err:
            print(f"[✖] Insert failed for {row['email']}: {err}")
    connection.commit()
    print(f"[✔] Inserted {inserted} new records.")
    cursor.close()


if __name__ == "__main__":
    try:
        root_conn = connect_db()
        create_database(root_conn)
        root_conn.close()

        db_conn = connect_to_prodev()
        create_table(db_conn)

        # Load CSV
        data = pd.read_csv('customers.csv')  # Ensure file exists
        insert_data(db_conn, data)

        db_conn.close()
    except mysql.connector.Error as err:
        print(f"[✖] MySQL error: {err}")