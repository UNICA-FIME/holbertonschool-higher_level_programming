#!/usr/bin/python3
"""
firts(): returns the first result of the query or None,
if there are no rows in the result.
"""

if __name__ == '__main__':
    import sys
    from model_state import Base, State
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker, Session

    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Session = sessionmaker(engine)
    session = Session()
    q = session.query(State).first()
    if q is None:
        print("Nothing")
    else:
        print("{}: {}".format(q.id, q.name))
