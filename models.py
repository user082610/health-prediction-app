"""
models.py - Database models for the Health Prediction Application.

Defines the Patient model with all required fields for storing
patient information and AI-generated health predictions.
"""

from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

# Initialize SQLAlchemy instance
db = SQLAlchemy()


class Patient(db.Model):
    """
    Patient model to store patient details and blood test results.
    The 'remarks' field stores AI-generated health predictions.
    """

    __tablename__ = 'patients'

    id = db.Column(db.Integer, primary_key=True)
    full_name = db.Column(db.String(100), nullable=False)
    date_of_birth = db.Column(db.Date, nullable=False)
    email = db.Column(db.String(120), nullable=False)

    # Blood test values
    glucose = db.Column(db.Float, nullable=False)       # in mg/dL
    haemoglobin = db.Column(db.Float, nullable=False)   # in g/dL
    cholesterol = db.Column(db.Float, nullable=False)    # in mg/dL

    # AI-generated health prediction
    remarks = db.Column(db.Text, default='')

    # Timestamps
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(
        db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow
    )

    def __repr__(self):
        return f'<Patient {self.full_name}>'
