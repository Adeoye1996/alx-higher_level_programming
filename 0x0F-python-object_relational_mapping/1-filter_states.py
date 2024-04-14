#!/usr/bin/python3
"""
Lists all states with a name starting with 'N' (uppercase N)
"""
import sys
import MySQLdb

def main():
    if len(sys.argv) != 4:
        print("Usage: {} <username> <password> <database>".format(sys.argv[0]))
        return

    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    try:
        db = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=username,
            passwd=password,
            db=database
        )
    except MySQLdb.Error as e:
        print("Error connecting to the database:", e)
        return

    cursor = db.cursor()

    try:
        cursor.execute("""
            SELECT *
            FROM states
            WHERE name LIKE BINARY 'N%'
            ORDER BY id ASC
        """)
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
