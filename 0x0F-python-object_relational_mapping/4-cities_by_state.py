#!/usr/bin/python3
'''
4-cities_by_state.py:
script that lists all cities from the database hbtn_0e_4_usa
Usage: ./4-cities_by_state.py <mysql username> <mysql password> <database name>
'''

import MySQLdb
from sys import argv

if __name__ == "__main__":
    db = MySQLdb.connect(user=argv[1], passwd=argv[2], db=argv[3],
                         host='localhost', port=3306, charset="utf8")
    cur = db.cursor()
    cur.execute("SELECT `cities`.`id`, `cities`.`name`, `states`.`name`\
                FROM `cities`\
                JOIN `states` ON `cities`.`state_id` = `states`.`id`\
                ORDER BY `cities`.`id`")
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()
