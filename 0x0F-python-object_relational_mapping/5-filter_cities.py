#!/usr/bin/python3
"""
script that takes in the name of a state as an argument
and lists all cities of that state
"""
import MySQLdb
import sys

if __name__ = "__main__":
    MySQLdb.connect(host="localhost", user=sys.argv[1], passwd=sys.argv[2], database=sys.argv[3], port=3306)
    cursor = db.cursor
    cursor.execute("SELECT cities.name FROM cities INER JOIN states ON states.id=cities.state|_id WHERE states.name=%s""", (sys.argv[4],))
    rows = cursor.fetchall()
    temp = list(row[0] for row in rows)
    print(*temp, sep=", ")
    cursor.close()
    db.close()
