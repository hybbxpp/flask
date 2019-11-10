from app import db

class Tasks(db.Model):
     id = db.Column(db.Integer,primary_key=True)

     title = db.Column(db.String(250), index=True)
     state = db.Column(db.String(250), index=True)
     year = db.Column(db.Date)
     def __repr__(self):
         return self.title + ' ' + self.state

class Finish(db.Model):
     id = db.Column(db.Integer,primary_key=True)

     title = db.Column(db.String(250), index=True)
     state = db.Column(db.String(250), index=True)
     year = db.Column(db.Date)

     def __repr__(self):
         return self.title + ' ' + self.state
