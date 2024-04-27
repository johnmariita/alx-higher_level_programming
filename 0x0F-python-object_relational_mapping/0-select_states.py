#!/usr/bin/python3
"""Module containing a script that lists states from a table"""
import sys
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", user=sys.argv[1],
                         port=3306, password=sys.argv[2], database=sys.argv[3])
    cu = db.cursor()
    cu.execute("SELECT * FROM states")
    rows = cu.fetchall()
    for row in rows:
        print(row)
    cu.close()
    db.close()
