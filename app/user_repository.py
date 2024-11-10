from sqlalchemy.orm import Session
from typing import List, Optional
from app.models import User, UserCreate

# Repository Interface
class UserRepositoryInterface:
    def get_user_by_username(self, db: Session, username: str) -> Optional[User]:
        pass

    def get_user_by_email(self, db: Session, email: str) -> Optional[User]:
        pass

    def get_users(self, db: Session, skip: int = 0, limit: int = 10) -> List[User]:
        pass

    def create_user(self, db: Session, user: UserCreate) -> User:
        pass

# UserRepository 구현체
class UserRepository(UserRepositoryInterface):
    def get_user_by_username(self, db: Session, username: str) -> Optional[User]:
        return db.query(User).filter(User.username == username).first()

    def get_user_by_email(self, db: Session, email: str) -> Optional[User]:
        return db.query(User).filter(User.email == email).first()

    def get_users(self, db: Session, skip: int = 0, limit: int = 10) -> List[User]:
        return db.query(User).offset(skip).limit(limit).all()

    def create_user(self, db: Session, user: UserCreate) -> User:
        db_user = User(
            username=user.username,
            email=user.email,
            full_name=user.full_name
        )
        db.add(db_user)
        db.commit()
        db.refresh(db_user)
        return db_user
