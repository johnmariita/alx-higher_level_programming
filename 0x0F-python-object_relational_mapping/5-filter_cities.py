#!/usr/bin/python3
"""A script that filters cities by states"""

import sys
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", user=sys.argv[1],
                         port=3306, password=sys.argv[2], database=sys.argv[3])
    cu = db.cursor()
    city = sys.argv[4].split("'")[0]
    cu.execute("SELECT cities.name FROM cities JOIN states \
               WHERE cities.state_id = states.id AND states.name=%s", (city, ))
    cities = [x[0] for x in cu.fetchall()]
    print(', '.join(cities))
