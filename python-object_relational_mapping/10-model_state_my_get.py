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
    q = session.query(State.id)
    q = q.filter(State.name == sys.argv[4]).order_by(State.id).all()
    if len(q) > 0:
        for item in range(0, len(q)):
            print(q[item][0])
    else:
        print("Not found")
