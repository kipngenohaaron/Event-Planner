# Event Planner - Flask Application

**Author**  
- **Kipngenoh Aaron Rotich**  
    - 📱 Contact: 0724828197 | 0724279400  
    - 📧 Email: kipngenoahaaron@gmail.com  
    - 🔗 GitHub: [https://github.com/kipngenohaaron](https://github.com/kipngenohaaron)

---

This is a simple event planning application built with **Flask** and **SQLAlchemy** to manage events. Users can create events by filling out a form with details such as title, description, date, and location.

## Features
- **Create Events**: Users can add new events to the database.
- **SQLite Database**: Events are stored in a local SQLite database (`events.db`).
- **Flask Web Framework**: Lightweight and easy to use for building web applications.

## Requirements

To run the Event Planner app locally, you need:

- Python 3.x
- Flask
- SQLAlchemy
- SQLite (installed with Python)

## Setup Instructions

### 1. Clone the Repository

Clone this repository to your local machine.

```bash
git clone https://github.com/kipngenohaaron/Event-Planner.git
cd Event-Planner
```

### 2. Create a Virtual Environment

To avoid conflicts with other projects, it’s recommended to use a virtual environment for this project.

```bash
python3 -m venv venv
```

### 3. Activate the Virtual Environment

- On **Linux/macOS**:

```bash
source venv/bin/activate
```

- On **Windows**:

```bash
venv\Scripts\activate
```

### 4. Install Dependencies

Install the required packages by running:

```bash
pip install -r requirements.txt
```

This will install **Flask**, **Flask-SQLAlchemy**, and other dependencies needed for the app to run.

### 5. Create the SQLite Database

Flask will automatically create the database for you on the first run, but you can manually create it using SQLite if needed.

- Ensure the `instance/` directory exists:

```bash
mkdir instance
```

- Then, run the following Python script to create the `events.db` file:

```python
from app import create_app, db
from app.models import Event

app = create_app()

with app.app_context():
    db.create_all()  # Creates the tables in the database
```

You can also open the SQLite database file using the SQLite CLI or any database management tool to check the data.

### 6. Run the Flask App

Start the Flask application using the following command:

```bash
python3 run.py
```

Flask will start the development server, and you can open your browser to access the app at:

```
http://127.0.0.1:5000
```

### 7. Access the Event Creation Page

Go to the URL:

```
http://127.0.0.1:5000/create
```

Here, you can fill out a form to create new events, which will be saved to the `events.db` database.

## File Structure

Your project should have the following file structure:

```
Event-Planner/
│
├── app/
│   ├── __init__.py       # App factory function and app setup
│   ├── models.py         # Database models (Event class)
│   ├── routes.py         # Routes and views for the app
│   ├── templates/        # HTML templates for the app
│   │   └── create_event.html  # Template for creating events
│   └── static/           # Static files (CSS, JS, images)
│
├── instance/
│   └── events.db         # SQLite database file
├── config.py             # Configurations for Flask and SQLAlchemy
├── requirements.txt      # List of dependencies
├── run.py                # Script to run the app
└── README.md             # Project documentation (this file)
```

## SQLite Database

- The app uses **SQLite** to store event data.
- The database is created in the `instance/` directory with the filename `events.db`.
- You can use a tool like **DB Browser for SQLite** or the SQLite command line tool to inspect the database.

### To Open the SQLite Database File:

#### Option 1: Using DB Browser for SQLite
1. Install **DB Browser for SQLite**: [Download link](https://sqlitebrowser.org/dl/).
2. Open the app and click **Open Database**.
3. Navigate to `instance/events.db` and open it to browse the tables and data.

#### Option 2: Using SQLite Command Line
1. Install SQLite3 if it's not installed:
   ```bash
   sudo apt install sqlite3
   ```
2. Open the terminal and run:
   ```bash
   sqlite3 instance/events.db
   ```

   This will open the SQLite shell. To list all tables, run:
   ```sql
   .tables
   ```

   To see the data in the `event` table:
   ```sql
   SELECT * FROM event;
   ```

#### Option 3: Using Python
You can also inspect the database by querying it directly in Python:

```python
from app import db
from app.models import Event

events = Event.query.all()
for event in events:
    print(event.title, event.description, event.date, event.location)
```

## Troubleshooting

### Common Issues

1. **"Database not found"**:
   - Ensure that the `instance/` folder exists and contains `events.db`. Flask will automatically create the database the first time the app is run.

2. **Missing SQLite command**:
   - Install `sqlite3` if it's not installed using `sudo apt install sqlite3` on Linux or the appropriate command for your system.

3. **Flask server error**:
   - If you see an error when running `python3 run.py`, check the terminal output for any specific issues. Common issues include database connection errors or missing environment variables.

## License

This project is open-source and available under the [MIT License](LICENSE).

