#!/usr/bin/python3
'''
2-my_filter_states.py:
script that takes in an argument and displays all values in the states
table of hbtn_0e_0_usa where name matches the argument.
Usage: ./2-my_filter_states.py <mysql username> <mysql password>
<database name> <state name searched>
'''

import MySQLdb
from sys import argv

if __name__ == "__main__":
    db = MySQLdb.connect(user=argv[1], passwd=argv[2], db=argv[3],
                         host='localhost', port=3306, charset="utf8")
    cur = db.cursor()
    cur.execute("SELECT * FROM `states` WHERE `name` LIKE BINARY '{}'"
                .format(argv[4]))
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()
