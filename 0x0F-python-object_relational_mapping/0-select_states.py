#!/usr/bin/python3
""" A script that lists all states from a database"""
import MySQLdb
import sys

if __name__ == "__main__":
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3]
    )

    cur = db.cursor()
    cur.execute("SELECT * FROM states")
    all_states = cur.fetchall()
    for each_state in all_states:
        print(each_state)
    cur.close()
    db.close()
