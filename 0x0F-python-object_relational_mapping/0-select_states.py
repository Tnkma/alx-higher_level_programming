#!/usr/bin/python3
""" A script that lists all states from a database"""
import MySQLdb
import sys

if __name__ == "__main__":
    mysql_user = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]

    connect_db = MySQLdb.connect(
        host='localhost',
        port=3306,
        user=mysql_user,
        passwd=mysql_password,
        db=database_name
    )

    cursor = connect_db.cursor()
    cursor.execute("SELECT * FROM states")
    all_states =cursor.fetchall()
    for each_state in all_states:
        print(each_state)
    cursor.close()
    db.close()
