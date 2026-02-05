from app.extensions import db

class role(db.Model):
    __tablename__ = 'roles'
    id_admin = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), nullable=False)
