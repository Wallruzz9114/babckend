from server import db
from server.api.users.models import User


def add_user(username, email):
    user = User(username=username, email=email)
    db.session.add(user)
    db.session.commit()
    return user


def recreate_db():
    db.session.remove()
    db.drop_all()
    db.create_all()
