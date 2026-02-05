from app.extensions import db

class conversion(db.Model):
    __tablename__ = 'conversion'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    from_currency = db.Column(db.String(3), nullable=False)
    to_currency = db.Column(db.String(3), nullable=False)
    rate = db.Column(db.Float, nullable=False)
    date = db.Column(db.DateTime, nullable=False)
    def __init__(self, user_id, from_currency, to_currency, rate, date):
        self.user_id = user_id
        self.from_currency = from_currency
        self.to_currency = to_currency
        self.rate = rate