from .. import db
from werkzeug.security import generate_password_hash, check_password_hash
from .. import login
from flask_login import UserMixin
from ..models import Audithories

class User(UserMixin, db.Model):
  __tablename__ = 'users'
  __table_args__ = {'extend_existing': True}
  id = db.Column(db.Integer, primary_key=True)
  username = db.Column(db.String(64), index=True, unique=True)
  email = db.Column(db.String(120), index=True, unique=True)
  is_teacher = db.Column(db.Boolean)
  password_hash = db.Column(db.String(128))
  audithories = db.relationship('Audithories', backref='author', lazy='dynamic')

  def __repr__(self):
    return '<User {}>'.format(self.username)

  def set_password(self, password):
    self.password_hash = generate_password_hash(password)

  def check_password(self, password):
    return check_password_hash(self.password_hash, password)

@login.user_loader
def load_user(id):
    return User.query.get(int(id))
