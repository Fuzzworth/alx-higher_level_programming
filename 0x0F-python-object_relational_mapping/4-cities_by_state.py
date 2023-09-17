#!/usr/bin/python3
"""
Module Docs
"""
from sys import argv
import MySQLdb


def main():
    """
    Function DOC
    """
    db_user = argv[1]
    db_password = argv[2]
    db_db = argv[3]
    db_host = "localhost"
    db_port = 3306

    try:
        qs = "SELECT cities.id, cities.name, states.name "
        qs += "FROM cities LEFT JOIN states "
        qs += "ON cities.state_id=states.id "
        qs += "ORDER BY cities.id ASC"
        conn = MySQLdb.connect(host=db_host, port=db_port,
                               user=db_user, passwd=db_password,
                               db=db_db, charset="utf8")
        cur = conn.cursor()
        cur.execute(qs)
        query_rows = cur.fetchall()
        for row in query_rows:
            print(row)
        cur.close()
        conn.close()
    except Exception:
        pass


if __name__ == "__main__":
    main()
