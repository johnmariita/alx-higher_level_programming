#!/usr/bin/python3
"""Module containing a script that lists states from a table
starting with N"""
import sys
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", user=sys.argv[1],
                         port=3306, password=sys.argv[2], database=sys.argv[3])
    cu = db.cursor()
    query = "SELECT * FROM states WHERE name='{}'".format(sys.argv[4])
    cu.execute(query + " COLLATE utf8mb4_bin")
    rows = cu.fetchall()
    for row in rows:
        print(row)
    cu.close()
    db.close()
