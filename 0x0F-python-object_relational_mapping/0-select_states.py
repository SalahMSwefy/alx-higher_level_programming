#!/usr/bin/python3
# 0-select_states.py:
# script that lists all states from the database hbtn_0e_0_usa


import MySQLdb
import sys

db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2],
                       db=sys.argv[3], host="localhost", port=3306)
cur = db.cursor()
cur.execute("SELECT * FROM states")
rows = cur.fetchall()
for row in rows:
    print(row)
