#!/usr/bin/python3
"""
engine: establece la conexión entre la aplicacion y gestor
Session: establece una relación entre la conexión y los modelos
session: es una instancia de mi clase.
session.query(State).order_by(State.id).all()
 session.query(State): es igual que el SELECT en sql
 session.query(State).order_by(State.id): ordena por id
 session.query(State).order_by(State.id).all(): selecciona todo la columna y ordena.
"""
import sys
from model_state import State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                       .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                       pool_pre_ping=True)

Session = sessionmaker(bind=engine)
session = Session()
q = session.query(State).order_by(State.id).all()
for state in q:
    print("{}: {}".format(state.id, state.name))
