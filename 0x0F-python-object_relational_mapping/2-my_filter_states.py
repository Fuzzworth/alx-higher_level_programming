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
    search_string = argv[4]

    query_string = "SELECT id, name FROM states WHERE "
    query_string += "name LIKE BINARY '{}' ORDER BY id ASC".format(
            search_string.strip("")
            )
    conn = MySQLdb.connect(host=db_host, port=db_port,
                           user=db_user, passwd=db_password,
                           db=db_db, charset="utf8")
    cur = conn.cursor()
    cur.execute(query_string)
    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)
    cur.close()
    conn.close()


if __name__ == "__main__":
    main()
