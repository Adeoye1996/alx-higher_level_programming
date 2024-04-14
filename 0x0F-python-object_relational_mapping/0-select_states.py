#!/usr/bin/python3
"""lists all states from the database hbtn_0e_0_usa
"""
import sys
import MySQLdb

if __name__ == "__main__":
    # Establish connection to MySQL database
    db = MySQLdb.connect(
            host="localhost",
            user=sys.argv[1],
            passwd=sys.argv[2],
            db=sys.argv[3],
            port=3306)

    # Create a cursor object
    cursor = db.cursor()
    # Execute the SQL query
    cursor.execute("""SELECT * FROM states ORDER BY id ASC""")
    # Fetch all the rows from the result
    result = cursor.fetchall()
    # Print each row
    for row in result:
        print(row)
