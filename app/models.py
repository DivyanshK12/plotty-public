from . import db

class Update(db.Model):
    __tablename__ = 'updates'
    id = db.Column(db.Integer, primary_key = True)
    user = db.Column(db.String(64), nullable = False)
    count = db.Column(db.Integer, nullable = False)
    date = db.Column(db.DateTime, nullable = False)

    def json(self):
        return {"user":self.user, "count":self.count, "date":self.date}