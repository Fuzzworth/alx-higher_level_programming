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
    state_name = argv[4]

    try:
        qs = """
            SELECT UNIQUE cities.name
            FROM states
            LEFT JOIN cities
            ON cities.state_id=(
                SELECT id
                FROM states
                WHERE states.name = %s
            )
            ORDER BY cities.id ASC
            """
        conn = MySQLdb.connect(host=db_host, port=db_port,
                               user=db_user, passwd=db_password,
                               db=db_db, charset="utf8")
        cur = conn.cursor()
        cur.execute(qs, (state_name, ))
        query_rows = cur.fetchall()
        if query_rows:
            list_result = []
            for row in query_rows:
                list_result.append(row[0])
            print(", ".join(list_result))
        cur.close()
        conn.close()
    except Exception:
        pass


if __name__ == "__main__":
    main()
