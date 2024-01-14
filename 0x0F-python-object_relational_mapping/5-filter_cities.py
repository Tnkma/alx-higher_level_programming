#!/usr/bin/python3
"""
takes in an argument and displays all values
in the states table of hbtn_0e_0_usa where name matches the argument.
"""
import MySQLdb
import sys


if __name__ == "__main__":
    user_name = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]

    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=user_name,
        passwd=password,
        db=db_name
    )
    curs = db.cursor()
    curs.execute("""SELECT cities.name FROM cities
                 JOIN states ON states.id=cities.state_id
                 WHERE states.name=%s""", (sys.argv[4],))
    matched_values = curs.fetchall()
    tmp = list(values[0] for values in matched_values)
    print(*tmp, sep=", ")
    curs.close()
    db.close()
