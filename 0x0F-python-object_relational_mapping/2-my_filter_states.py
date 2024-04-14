#!/usr/bin/python3
"""
Displays all values in the states table of the specified database where
name matches the provided state name
"""
import sys
import MySQLdb


def main():
    if len(sys.argv) != 5:
        print("Usage: {} <username> <password> <database> <state_name>"
              .format(sys.argv[0]))
        return

    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state_name = sys.argv[4]

    try:
        db = MySQLdb.connect(
            host="localhost",
            user=username,
            passwd=password,
            db=database,
            port=3306
        )
    except MySQLdb.Error as e:
        print("Error connecting to the database:", e)
        return

    cursor = db.cursor()

    try:
        query = """
            SELECT *
            FROM states
            WHERE name LIKE BINARY '{}'
            ORDER BY id ASC
        """.format(state_name)
        cursor.execute(query)
        results = cursor.fetchall()
        for row in results:
            print(row)
    except MySQLdb.Error as e:
        print("Error executing query:", e)
    finally:
        cursor.close()
        db.close()


if __name__ == "__main__":
    main()
