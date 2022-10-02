from peakbagger import db

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    notes = db.Column(db.String(100), nullable=False)
    link = db.Column(db.String(100), nullable=False)



