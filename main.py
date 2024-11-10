from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from app.database import get_db, create_tables
from app.models import UserCreate, UserResponse
from app.user_service import UserService
from app.user_repository import UserRepository
from typing import List

# Create tables before the app starts
create_tables()

app = FastAPI()

# Repository와 Service를 의존성 주입으로 설정
def get_user_service(repo=Depends(UserRepository)):
    return UserService(repo)

# Create User API Endpoint
@app.post("/users/", response_model=UserResponse)
def create_user_endpoint(
    user: UserCreate,
    db: Session = Depends(get_db),
    service: UserService = Depends(get_user_service)
):
    return service.create_user(db, user)

# Get Users API Endpoint
@app.get("/users/", response_model=List[UserResponse])
def read_users(
    skip: int = 0,
    limit: int = 10,
    db: Session = Depends(get_db),
    service: UserService = Depends(get_user_service)
):
    return service.get_users(db, skip, limit)

# Get User by Username API Endpoint
@app.get("/users/{username}", response_model=UserResponse)
def read_user(
    username: str,
    db: Session = Depends(get_db),
    service: UserService = Depends(get_user_service)
):
    return service.get_user_by_username(db, username)
