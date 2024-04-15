#!/usr/bin/python3
"""
Script: 1-filter_states.py
Connects to a MySQL database and retrieves all states with names starting with 'N'.
Sorts the results by state ID in ascending order.
"""

import MySQLdb
import sys

if __name__ == "__main__":
    # Check if the correct number of arguments is provided
    if len(sys.argv) != 4:
        print("Usage: {} mysql_username mysql_password db_name".format(sys.argv[0]))
        sys.exit(1)

    # Extract MySQL username, password, and database name from command line arguments
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    db_name = sys.argv[3]

    try:
        # Connect to the MySQL database
        conn = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=mysql_username,
            passwd=mysql_password,
            db=db_name,
            charset="utf8"
        )
    except MySQLdb.Error as e:
        # Handle connection errors
        print("Error connecting to database: {}".format(e))
        sys.exit(1)

    # Create a cursor object to execute SQL queries
    cur = conn.cursor()

    # Execute the SQL query to select states starting with 'N' and order by ID
    cur.execute("SELECT * FROM states WHERE name LIKE BINARY 'N%' ORDER BY states.id ASC")

    # Fetch all the rows from the query result
    rows = cur.fetchall()

    # Print the retrieved rows
    for row in rows:
        print(row)

    # Close the cursor and database connection
    cur.close()
    conn.close()
