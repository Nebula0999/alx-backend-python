import mysql.connector

def stream_user_ages():
    """
    Generator that yields one user age at a time from the database.
    """
    connection = mysql.connector.connect(
        host="localhost",
        user="Nebula",
        password="Nebula@2025",
        database="ALX_prodev"
    )
    cursor = connection.cursor()

    cursor.execute("SELECT age FROM user_data")  # ✅ No AVG used

    for (age,) in cursor:  # ✅ Loop 1
        yield float(age)

    cursor.close()
    connection.close()


def calculate_average_age():
    """
    Calculates and prints the average age using the stream_user_ages generator.
    """
    total = 0
    count = 0

    for age in stream_user_ages():  # ✅ Loop 2
        total += age
        count += 1

    if count > 0:
        average = total / count
        print(f"Average age of users: {average:.2f}")
    else:
        print("No users found.")


if __name__ == "__main__":
    calculate_average_age()
