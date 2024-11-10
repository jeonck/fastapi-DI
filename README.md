# fastapi-DI

A FastAPI project with Dependency Injection.

## Project Structure
```
fastapi-DI/
├── app/
│   ├── __init__.py
│   └── database.py
├── main.py
└── README.md
```

## Installation
```bash
pip install fastapi uvicorn sqlalchemy
```

## Running the Application
Make sure you're in the project root directory and run:
```bash
uvicorn main:app --reload
```

## Development
To avoid import errors, ensure that:
1. Your project has proper `__init__.py` files in each directory
2. You run the application from the project root directory

# API 테스트
```bash
curl -X POST http://127.0.0.1:8000/users/ -H "Content-Type: application/json" -d '{"username": "testuser", "email": "testuser@example.com", "full_name": "Test User", "password": "testpassword"}'
```
