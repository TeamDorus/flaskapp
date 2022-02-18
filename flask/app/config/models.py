from app import db


class TraccarEvent(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.String(25), unique=True, nullable=False)
    status = db.Column(db.String(5), nullable=False)

    def __repr__(self):
        return f"TraccarEvent( '{self.type}', '{self.status}')"

