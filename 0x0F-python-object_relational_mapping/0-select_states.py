#!/usr/bin/python3
""" A script that lists all states from a database"""
import MySQLdb
import sys

if __name__ == "__main__":
    user_name = sys.argv[1]
    mysql_password = sys.argv[2]
    db_name = sys.argv[3]

    connect_db = MySQLdb.connect(
            host = 'localhost',
            port=3306,
            user = user_name,
            passwd = mysql_password,
            db = db_name
            )
    cursor = connect_db.cursor()
    cursor.execute("SELECT * FROM states")
    all_states =cursor.fetchall()
    for each_state in all_states:
        print(each_state)
    cursor.close()
    db.close()
