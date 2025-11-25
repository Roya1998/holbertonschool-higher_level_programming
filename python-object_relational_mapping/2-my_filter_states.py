#!/usr/bin/python3
"""
Script that takes in an argument and displays all values in the states
table of hbtn_0e_0_usa where name matches the argument.
"""

import MySQLdb
import sys


if __name__ == "__main__":
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]
    state_name_searched = sys.argv[4]

    db = None

    try:
        db = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=mysql_username,
            passwd=mysql_password,
            db=database_name,
            charset="utf8"
        )

        cur = db.cursor()

        query = (
            "SELECT * FROM states WHERE BINARY name = '{}' "
            "ORDER BY id ASC"
        ).format(state_name_searched)

        cur.execute(query)
        rows = cur.fetchall()

        for row in rows:
            print(row)

        cur.close()

    except MySQLdb.Error as e:
        print(f"MySQL Error: {e}")

    finally:
        if db:
            db.close()