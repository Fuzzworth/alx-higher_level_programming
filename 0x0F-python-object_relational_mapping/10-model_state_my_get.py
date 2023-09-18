#!/usr/bin/python3
"""
Module Docs
"""
from sys import argv
from model_state import Base, State
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
    search_string = argv[4]

    try:
        engine = create_engine(
                'mysql+mysqldb://{}:{}@{}/{}'
                .format(db_user,
                        db_password,
                        db_host,
                        db_db),
                pool_pre_ping=True)
        Base.metadata.create_all(engine)
        Session = sessionmaker(bind=engine)
        session = Session(engine)
        state = session.query(State).filter(State.name == argv[4]).first()
        if state:
            print(state.id)
        else:
            print("Not found")
        session.close()
    except Exception:
        pass


if __name__ == "__main__":
    main()
