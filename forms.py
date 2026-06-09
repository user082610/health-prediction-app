"""
forms.py - WTForms form definitions with validation rules.

Handles input validation for patient data including:
- Required field checks
- Email format validation
- Date of birth cannot be in the future
- Blood test values must be within valid numeric ranges
"""

from flask_wtf import FlaskForm
from wtforms import StringField, DateField, FloatField
from wtforms.validators import DataRequired, Email, NumberRange, ValidationError
from datetime import date


class PatientForm(FlaskForm):
    """Form for creating and editing patient records with validation."""

    full_name = StringField(
        'Full Name',
        validators=[
            DataRequired(message="Full name is required.")
        ]
    )

    date_of_birth = DateField(
        'Date of Birth',
        validators=[
            DataRequired(message="Date of birth is required.")
        ]
    )

    email = StringField(
        'Email Address',
        validators=[
            DataRequired(message="Email address is required."),
            Email(message="Please enter a valid email address.")
        ]
    )

    glucose = FloatField(
        'Glucose (mg/dL)',
        validators=[
            DataRequired(message="Glucose value is required."),
            NumberRange(
                min=0, max=1000,
                message="Glucose must be between 0 and 1000 mg/dL."
            )
        ]
    )

    haemoglobin = FloatField(
        'Haemoglobin (g/dL)',
        validators=[
            DataRequired(message="Haemoglobin value is required."),
            NumberRange(
                min=0, max=30,
                message="Haemoglobin must be between 0 and 30 g/dL."
            )
        ]
    )

    cholesterol = FloatField(
        'Cholesterol (mg/dL)',
        validators=[
            DataRequired(message="Cholesterol value is required."),
            NumberRange(
                min=0, max=1000,
                message="Cholesterol must be between 0 and 1000 mg/dL."
            )
        ]
    )

    def validate_date_of_birth(self, field):
        """Custom validator: Date of birth cannot be a future date."""
        if field.data and field.data > date.today():
            raise ValidationError("Date of birth cannot be a future date.")
