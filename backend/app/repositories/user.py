from sqlalchemy import select
from sqlalchemy.orm import Session

from app.models.user import User


class UserRepository:

    def get_by_email(
        self,
        db: Session,
        email: str,
    ) -> User | None:

        statement = select(User).where(
            User.email == email
        )

        result = db.execute(statement)

        return result.scalar_one_or_none()

    def create(
        self,
        db: Session,
        user: User,
    ) -> User:

        db.add(user)
        db.commit()
        db.refresh(user)

        return user


    def get_by_id(
        self,
        db: Session,
         user_id: str,
    ) -> User | None:

     statement = select(User).where(
        User.id == user_id
    )

     result = db.execute(statement)

     return result.scalar_one_or_none()
    


user_repository = UserRepository()