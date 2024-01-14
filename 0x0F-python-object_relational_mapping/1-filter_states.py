#!/usr/bin/python3
"""
prints all state with a name starting with N
"""
import MySQLdb
import sys

if __name__ == " __main__ ":
    user_name = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]

    connect_db = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=user_name,
            passwd=password,
            db=db_name
            )
    curs = connect_db.cursor()
    curs.execute("SELECT * FROM states WHERE name LIKE 'N%'")
    selected_states = fetchall()
    for states in selected_states:
        print(states)
    curs.close()
    db.close()
