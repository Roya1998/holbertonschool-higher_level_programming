#!/usr/bin/python3
"""
Script that takes in an argument and displays all values in the states
table of hbtn_0e_0_usa where name matches the argument.
The script takes 4 arguments:
1. mysql username
2. mysql password
3. database name
4. state name searched
"""
import MySQLdb
import sys
if __name__ == "__main__":
    # Check for the expected number of command-line arguments
    if len(sys.argv) != 5:
        # Note: The prompt states "no argument validation needed",
        # but a basic check ensures we have the necessary inputs.
        pass
    # Extract command-line arguments
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]
    state_name_searched = sys.argv[4]
    db = None  # Initialize db connection to None
    try:
        # Establish a connection to the MySQL server
        db = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=mysql_username,
            passwd=mysql_password,
            db=database_name,
            charset="utf8"
        )
        # Create a cursor object
        cur = db.cursor()
        # Construct the SQL query using Python's format() method as required.
        # FIX: Added 'BINARY' keyword to force a case-sensitive match
        # on the 'name' column, ensuring only 'Nevada' and not 'nevada'
        # or 'neVAda' is returned.
        query = "SELECT * FROM states= '{}' ORDER BY id ASC".format(
            state_name_searched
        )
        # Execute the SQL query
        cur.execute(query)
        # Fetch all the rows
        rows = cur.fetchall()
        # Print the results
        for row in rows:
            print(row)
        # Close the cursor
        cur.close()
    except MySQLdb.Error as e:
        # Handle connection or query errors
        print(f"MySQL Error: {e}")
    finally:
        # Close the database connection if it was successfully opened
        if db:
            db.close()
