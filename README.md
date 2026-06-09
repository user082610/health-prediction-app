# MIRA Health — AI-Powered Health Prediction Application

A full-stack health prediction application that uses **AI/ML** to analyze patient blood test results and predict possible health conditions. Built as part of the **MIRA (Medical Intelligence Robotic Automation)** project.

## Features

- **CRUD Operations** — Create, Read, Update, and Delete patient records
- **AI-Powered Predictions** — Integrates with Google Gemini AI to analyze blood test results (Glucose, Haemoglobin, Cholesterol) and generate health risk assessments
- **Data Validation** — Server-side validation for email format, date of birth (no future dates), and numeric blood test ranges
- **Persistent Storage** — SQLite database for reliable data storage
- **Clean UI** — Responsive Bootstrap 5 interface with a medical theme

## Tech Stack

| Layer      | Technology                          |
|------------|-------------------------------------|
| Backend    | Python, Flask, Flask-SQLAlchemy     |
| Frontend   | HTML5, CSS3, Bootstrap 5, Jinja2    |
| Database   | SQLite (via SQLAlchemy ORM)         |
| AI/ML API  | Google Gemini API (gemini-2.0-flash)|
| Validation | Flask-WTF, WTForms                 |

## Project Structure

```
├── app.py                  # Main Flask application with routes
├── models.py               # SQLAlchemy database models
├── forms.py                # WTForms form definitions + validation
├── ai_service.py           # Google Gemini AI integration
├── requirements.txt        # Python dependencies
├── .env.example            # Example environment variables
├── .gitignore              # Git ignore rules
├── templates/
│   ├── base.html           # Base layout template
│   ├── index.html          # Patient records list
│   ├── add_patient.html    # Add new patient form
│   ├── edit_patient.html   # Edit patient form
│   └── view_patient.html   # View patient details
└── static/
    └── css/
        └── style.css       # Custom styles
```

## Setup Instructions

### Prerequisites

- Python 3.8 or higher
- Google Gemini API key (free from [Google AI Studio](https://aistudio.google.com/apikey))

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/user082610/health-prediction-app.git
   cd health-prediction-app
   ```

2. **Create a virtual environment**
   ```bash
   python3 -m venv venv
   source venv/bin/activate        # macOS/Linux
   venv\Scripts\activate           # Windows
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables**
   ```bash
   cp .env.example .env
   ```
   Open `.env` and add your API key:
   ```
   GEMINI_API_KEY=your_actual_api_key_here
   SECRET_KEY=any_random_string_here
   ```

5. **Run the application**
   ```bash
   python app.py
   ```

6. **Open in browser**
   ```
   http://127.0.0.1:5000
   ```

## How It Works

1. **Add a Patient** — Enter patient details (name, DOB, email) and blood test values (glucose, haemoglobin, cholesterol).
2. **AI Prediction** — On submission, the blood test values are sent to Google Gemini AI, which analyzes them against normal ranges and generates a health risk assessment.
3. **View Results** — The AI prediction is displayed in the "Remarks" field, along with color-coded badges showing whether each value is normal or abnormal.
4. **Manage Records** — Edit patient data, regenerate AI predictions, or delete records as needed.

## API Integration

The application uses the **Google Gemini API** (`gemini-2.0-flash` model) to generate health predictions. The AI receives:
- Blood test values with their normal reference ranges
- A structured prompt requesting a concise health assessment

The response is stored in the `remarks` field of each patient record.

## Screenshots

*Screenshots will be added after demo recording.*

## Author

Samyuktha Nagaraj
