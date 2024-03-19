#!/usr/bin/python3

import MySQLdb
import sys

def list_states(username, password, db_name):

    db = MySQLdb.connect(host="localhost", port=3306, user=username, passwd=password, db=db_name)

    cursor =db.cursor()

    cursor.execute("SELECT * FROM states ORDER BY states.id ASC")

    states = cursor.fetchall()

    for state in states:
        print(state)

    cursor.close()
    db.close()


if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]

    list_states(username, password, db_name)
