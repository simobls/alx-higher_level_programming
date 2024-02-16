#!/usr/bin/python3
"""Lists states"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    conn = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                           passwd=argv[2], db=argv[3], charset="utf8")
    cur = conn.cursor()
    query = "SELECT GROUP_CONCAT(c.name SEPARATOR ', ') " + \
        "FROM cities c INNER JOIN states s " + \
        "ON s.id = c.state_id " + \
        "WHERE s.name = '{}'".format(argv[4])
    cur.execute(query)
    query_rows = cur.fetchall()
    for row in query_rows:
        print(row[0])
    cur.close()
    conn.close()
