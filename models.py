from database import db

class CRMMapping(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    crm_name = db.Column(db.String(50), unique=True, nullable=False)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    phone = db.Column(db.String(20), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    company_name = db.Column(db.String(100), nullable=False)
    phone_consent = db.Column(db.Boolean, nullable=False)
    email_consent = db.Column(db.Boolean, nullable=False)
