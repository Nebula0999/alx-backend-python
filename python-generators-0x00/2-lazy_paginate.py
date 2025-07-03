import mysql.connector

def paginate_users(page_size, offset):
    """
    Fetch a single page of users starting from the offset.
    """
    connection = mysql.connector.connect(
        host="localhost",
        user="your_mysql_user",
        password="your_mysql_password",
        database="ALX_prodev"
    )
    cursor = connection.cursor(dictionary=True)
    
    cursor.execute(
        "SELECT * FROM user_data ORDER BY user_id LIMIT %s OFFSET %s",
        (page_size, offset)
    )
    result = cursor.fetchall()

    cursor.close()
    connection.close()
    return result


def lazy_paginate(page_size):
    """
    Generator that lazily paginates user_data table using one loop.
    """
    offset = 0
    while True:  # ✅ Only loop allowed
        page = paginate_users(page_size, offset)
        if not page:
            break
        yield page
        offset += page_size

if __name__ == "__main__":
    for page in lazy_paginate(3):
        print("Page:")
        for user in page:
            print(user)
