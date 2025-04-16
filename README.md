# My Fitness App

A Django RESTful API for logging meals, tracking workouts, and monitoring daily fitness progress.

---

## Features

- User registration and login
- Add, view, update, and delete meals
- Add, view, and delete workouts
- Get daily summaries of calorie intake and workouts
- Token-based authentication using Django's auth system

---

## Tech Stack

- Python
- Django
- Django REST Framework
- SQLite (default) or PostgreSQL

---

## Getting Started

### Prerequisites

- Python 3.8+
- pip
- Virtualenv (optional but recommended)

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/Ivaylo1992/my-fitness-app.git
   cd my-fitness-app
2. **Create a virtual environment**
   ```bash
   python3 -m venv venv # On Windows: python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
4. **Apply migrations**
   ```bash
   python3 manage.py makemigrations # On Windows: python manage.py makemigrations
4. **Run the development server**
   ```bash
   python manage.py runserver

## API Endpoints

| Method | Endpoint               | Description                      |
|--------|------------------------|----------------------------------|
| POST   | /api/auth/register/    | Register a new user              |
| POST   | /api/auth/login/       | Log in a user                    |
| GET    | /api/meals/            | List all meals                   |
| POST   | /api/meals/            | Add a new meal                   |
| PUT    | /api/meals/<id>/       | Update a meal                    |
| DELETE | /api/meals/<id>/       | Delete a meal                    |
| GET    | /api/workouts/         | List all workouts                |
| POST   | /api/workouts/         | Add a new workout                |
| DELETE | /api/workouts/<id>/    | Delete a workout                 |
| GET    | /api/summary/          | Get daily summary of activities  |

## Running Tests

To run the unit tests for the project, use the following command:

```bash
python manage.py test

