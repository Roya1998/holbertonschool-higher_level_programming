#!/usr/bin/python3
"""
Lists all cities of a given state from hbtn_0e_4_usa (safe from SQL injections).
"""
import MySQLdb
import sys
if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]
    state_name = sys.argv[4]
    # Connect to MySQL
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=db_name
    )
    cursor = db.cursor()
    # Safe parameterized query (SQL injection proof)
    query = """
        SELECT cities.name
        FROM cities
        JOIN states ON cities.state_id = states.id
        WHERE states.name = %s
        ORDER BY cities.id ASC;
    """
    cursor.execute(query, (state_name,))
    rows = cursor.fetchall()
    # Extract city names
    city_names = [row[0] for row in rows]
    # Print exactly like project example
    print(", ".join(city_names))
    cursor.close()
    db.close()
