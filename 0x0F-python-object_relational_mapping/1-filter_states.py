#!/usr/bin/python3

import MySQLdb
import sys

def list_state(username, password, db_name):
    """
    script that lists all states with a name starting with N (upper N) from the database hbtn_0e_0_usa
    """
    db = MySQLdb.connect(host="localhost", user=username, passwd=password, port=3306, database=db_name)
    cursor = db.cursor()

    cursor.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY states.id ASC")

    states = cursor.fetchall()

    for state in states:
        print(state)

    cursor.close()
    db.close()

if __name__ == "__main__":
    """
    Entry point
    """
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]

    list_state(username, password, db_name)
