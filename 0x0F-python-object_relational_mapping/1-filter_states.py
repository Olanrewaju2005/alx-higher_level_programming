#!/usr/bin/python3

import MySQLdb
import sys

if __name__ == "__main__":
    """
    Entry point
    """
    db = MySQL.connect(host="localhost", user=sys.argv[1], passwd=sys.argv[2], database=sys.argv[3], port=3306)
    cursor = db.cursor()

    cursor.execute("""SELECT * FROM states WHERE name LIKE 'N%' ORDER BY states.id ASC""")

    states = cursor.fetchall()

    for state in states:
        print(state)

    cursor.close()
    db.close()
