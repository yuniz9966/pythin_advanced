from models_relations import User
from db_connection import DBConnection

from SQLAlchemy_lesson.sqlalchemy_train import engine

user = User(...)

with DBConnection(engine) as session:
    session.add(user)