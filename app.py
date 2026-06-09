"""
app.py - Main Flask application for the Health Prediction App.

This is the entry point of the application. It sets up the Flask server,
configures the database, and defines all the routes for CRUD operations.
"""

from flask import Flask, render_template, redirect, url_for, flash, request
from models import db, Patient
from forms import PatientForm
from ai_service import get_health_prediction
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# ----- App Configuration -----
app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'dev-secret-key-change-in-production')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///patients.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database with the Flask app
db.init_app(app)

# Create all database tables on first run
with app.app_context():
    db.create_all()


# ----- Routes -----

@app.route('/')
def index():
    """Home page — displays all patient records in a table."""
    patients = Patient.query.order_by(Patient.created_at.desc()).all()
    return render_template('index.html', patients=patients)


@app.route('/add', methods=['GET', 'POST'])
def add_patient():
    """Add a new patient record with AI-generated health prediction."""
    form = PatientForm()

    if form.validate_on_submit():
        # Call the AI service to generate health prediction
        remarks = get_health_prediction(
            form.glucose.data,
            form.haemoglobin.data,
            form.cholesterol.data
        )

        # Create a new patient record
        patient = Patient(
            full_name=form.full_name.data,
            date_of_birth=form.date_of_birth.data,
            email=form.email.data,
            glucose=form.glucose.data,
            haemoglobin=form.haemoglobin.data,
            cholesterol=form.cholesterol.data,
            remarks=remarks
        )

        # Save to database
        db.session.add(patient)
        db.session.commit()

        flash('Patient record added successfully!', 'success')
        return redirect(url_for('index'))

    return render_template('add_patient.html', form=form)


@app.route('/view/<int:id>')
def view_patient(id):
    """View detailed information for a single patient."""
    patient = Patient.query.get_or_404(id)
    return render_template('view_patient.html', patient=patient)


@app.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit_patient(id):
    """Edit an existing patient record."""
    patient = Patient.query.get_or_404(id)
    form = PatientForm(obj=patient)

    if form.validate_on_submit():
        # Update patient fields
        patient.full_name = form.full_name.data
        patient.date_of_birth = form.date_of_birth.data
        patient.email = form.email.data
        patient.glucose = form.glucose.data
        patient.haemoglobin = form.haemoglobin.data
        patient.cholesterol = form.cholesterol.data

        # Regenerate AI remarks if the user checked the option
        if request.form.get('regenerate_remarks'):
            patient.remarks = get_health_prediction(
                form.glucose.data,
                form.haemoglobin.data,
                form.cholesterol.data
            )

        # Save changes
        db.session.commit()

        flash('Patient record updated successfully!', 'success')
        return redirect(url_for('view_patient', id=patient.id))

    return render_template('edit_patient.html', form=form, patient=patient)


@app.route('/delete/<int:id>', methods=['POST'])
def delete_patient(id):
    """Delete a patient record."""
    patient = Patient.query.get_or_404(id)
    db.session.delete(patient)
    db.session.commit()

    flash('Patient record deleted successfully!', 'success')
    return redirect(url_for('index'))


# ----- Run the App -----
if __name__ == '__main__':
    app.run(debug=True)
