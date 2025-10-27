from core import db

class Users(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(50), nullable=False)
  audithories = db.relationship('Audithories', lazy="dynamic")
  locale = db.Column(db.String(8))
  email = db.Column(db.String(50))
  def __repr__(self):
    return '<Users {}>'.format(self.title)

class Audithories(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(50))
  reason = db.Column(db.String(140))
  date = db.Column(db.Date())
  time = db.Column(db.Time())
  number = db.Column(db.Integer)
  user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    
  def __repr__(self):
    return '<Audithories {}>'.format(self.title)