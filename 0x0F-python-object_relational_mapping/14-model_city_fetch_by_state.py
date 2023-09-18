#!/usr/bin/python3
"""
Module Docs
"""
from sys import argv
from model_state import Base, State
from model_city import City
from sqlalchemy import (create_engine)
from sqlalchemy.orm import Session, sessionmaker


def main():
    """
    Function DOC
    """
    db_user = argv[1]
    db_password = argv[2]
    db_db = argv[3]
    db_host = "localhost"

    engine = create_engine(
            'mysql+mysqldb://{}:{}@{}/{}'
            .format(db_user,
                    db_password,
                    db_host,
                    db_db),
            pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    query_rows = session.query(State, City).join(City).order_by(City.id).all()
    for state, city in query_rows:
        print('{}: ({}) {}'.format(state.name, city.id, city.name))
    session.close()


if __name__ == "__main__":
    main()
