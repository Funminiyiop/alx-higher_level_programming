#!/usr/bin/python3
"""
This script takes in an argument and
displays all values in the states
where `name` matches the argument
from the database `hbtn_0e_0_usa`.
"""


def main(args):
    """
    Get all states from database by 
    name if match presented argument.
    """
    if len(args) != 5:
        raise Exception("need 4 arguments!")
    db = MySQLdb.connect(host='localhost',
                         user=args[1],
                         passwd=args[2],
                         db=args[3])
    cur = db.cursor()
    cur.execute(
        "SELECT * FROM states WHERE name LIKE '{}' ORDER BY id ASC"
        .format(args[4]))
    states = cur.fetchall()
    for state in states:
        if state[1] == args[4]:
            print(state)


if __name__ == "__main__":
    import sys
    import MySQLdb
    main(sys.argv)
