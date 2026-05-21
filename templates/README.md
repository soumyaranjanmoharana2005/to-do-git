# To-Do App using Flask and SQLite

A simple one-page To-Do app built with Flask and SQLite, using SQLAlchemy as the ORM.

## Features

- Add tasks
- Mark tasks as done or undone
- Delete tasks
- Timestamp on every task

## Tech Stack

- **Flask** — web framework
- **SQLite** — database
- **SQLAlchemy** — database ORM (via Flask-SQLAlchemy)
- **Jinja2** — HTML templating

## Project Structure

```
to-do/
├── app.py              # Flask routes
├── database.py         # Database models
├── templates/
│   └── index.html      # Frontend template
├── requirements.txt    # Dependencies
└── .gitignore
```

## Setup and Run

### 1. Clone the repository

```bash
git clone https://github.com/soumyaranjanmoharana2005/To-Do-app-using-flask-and-sqlite.git
cd To-Do-app-using-flask-and-sqlite
```

### 2. Create and activate a virtual environment

```bash
python3 -m venv ~/.venvs/to-do
source ~/.venvs/to-do/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the app

```bash
python3 app.py
```

### 5. Open in browser

```
http://localhost:5000
```
