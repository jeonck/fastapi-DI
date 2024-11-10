from sqlalchemy.orm import Session
from app.user_repository import UserRepositoryInterface
from app.models import UserCreate, User
from fastapi import HTTPException
from typing import List

class UserService:
    def __init__(self, repository: UserRepositoryInterface):
        self.repository = repository

    def create_user(self, db: Session, user: UserCreate) -> User:
        db_user = self.repository.get_user_by_email(db, user.email)
        if db_user:
            raise HTTPException(status_code=400, detail="Email already registered")
        return self.repository.create_user(db, user)

    def get_users(self, db: Session, skip: int = 0, limit: int = 10) -> List[User]:
        return self.repository.get_users(db, skip, limit)

    def get_user_by_username(self, db: Session, username: str) -> User:
        user = self.repository.get_user_by_username(db, username)
        if user is None:
            raise HTTPException(status_code=404, detail="User not found")
        return user
