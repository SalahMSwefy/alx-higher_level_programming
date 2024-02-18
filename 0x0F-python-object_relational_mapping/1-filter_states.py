#!/usr/bin/python3
'''
1-filter_states.py:
script that lists all states with a name starting with N
(upper N) from the database hbtn_0e_0_usa
Usage: ./1-filter_states.py <mysql username> <mysql password> <database name>
'''

import MySQLdb
from sys import argv

if __name__ == "__main__":
    db = MySQLdb.connect(user=argv[1], passwd=argv[2], db=argv[3],
                         host='localhost', port=3306, charset="utf8")
    cur = db.cursor()
    cur.execute("SELECT * FROM `states` WHERE `name` LIKE\
                BINARY 'N%' ORDER BY `id`")
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()
