## This project sets up a MySQL database called `ALX_prodev` and populates a `user_data` table with records from a CSV file. It is part of a backend engineering exercise to practice SQL scripting, Python data loading, and database interaction.

---

## Objective

- Create a MySQL database and table via Python
- Load user records from a CSV file (`user_data.csv`)
- Insert records only if they don’t already exist
- Generate a unique UUID for each user as `user_id`
- Stream and process data row-by-row for performance and scalability

## Database Setup
Connects to MySQL

Creates database ALX_prodev if it doesn't exist

Creates table user_data with:

user_id (UUID, PK, Indexed)

name (VARCHAR, NOT NULL)

email (VARCHAR, NOT NULL, UNIQUE)

age (DECIMAL)

Loads rows from CSV using pandas

Inserts them one by one using a UUID for user_id

Skips existing records using INSERT IGNORE