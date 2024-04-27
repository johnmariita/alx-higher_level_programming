#!/usr/bin/python3
"""A script that lists all the cities with their states"""

import sys
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", user=sys.argv[1],
                         port=3306, password=sys.argv[2], database=sys.argv[3])
    cu = db.cursor()
    cu.execute("SELECT cities.id, cities.name, states.name FROM cities \
               JOIN states WHERE cities.state_id=states.id")
    rows = cu.fetchall()
    for row in rows:
        print(row)
    cu.close()
    db.close()
