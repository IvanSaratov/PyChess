from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

from app import db, login


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.VARCHAR(64), index=True, unique=True)
    email = db.Column(db.VARCHAR(128), index=True, unique=True)
    password_hash = db.Column(db.String(256))
    first_name = db.Column(db.VARCHAR(64))
    last_name = db.Column(db.VARCHAR(64))

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)


@login.user_loader
def load_user(id):
    return User.query.get(int(id))


association_task_table = db.Table('task_association',
                                  db.Column('set_id', db.Integer, db.ForeignKey('set.id')),
                                  db.Column('task_id', db.Integer, db.ForeignKey('task.id'))
                                  )


class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.VARCHAR(64), unique=True)
    start_pos = db.Column(db.String(128))
    end_pos = db.Column(db.String(128))


class Set(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.VARCHAR(64), unique=True)
    tasks = db.relationship('Task', secondary=association_task_table,
                            primaryjoin=(association_task_table.c.task_id == id),
                            secondaryjoin=(association_task_table.c.set_id == id),
                            backref=db.backref('association_task_table', lazy='dynamic'), lazy='dynamic')
