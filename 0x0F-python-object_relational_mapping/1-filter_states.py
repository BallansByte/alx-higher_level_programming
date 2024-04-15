#!/usr/bin/python3

"""
Script: 1-filter_states.py
Connects to a MySQL database and retrieves all states with names starting with 'N'.
Sorts the results by state ID in ascending order.
"""

import MySQLdb
import sys

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: {} mysql_username mysql_password db_name".format(sys.argv[0]))
        sys.exit(1)

    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    db_name = sys.argv[3]

    try:
        conn = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=mysql_username,
            passwd=mysql_password,
            db=db_name,
            charset="utf8"
        )
    except MySQLdb.Error as e:
        print("Error connecting to database: {}".format(e))
        sys.exit(1)

    cur = conn.cursor()

    cur.execute("SELECT * FROM states WHERE name LIKE BINARY 'N%' ORDER BY states.id ASC")

     rows = cur.fetchall()

     for row in rows:
        print(row)

    cur.close()
    conn.close()
