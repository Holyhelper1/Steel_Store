from app.dao.base import BaseDao
from app.users.models import User
from app.database import async_session_maker
from sqlalchemy import select

class UsersDao(BaseDao):
    model = User

    @classmethod
    async def update_refresh_token(cls, user_id: str, token: str):
        async with async_session_maker() as session:
            query = select(cls.model).filter_by(id=user_id)
            result = await session.execute(query)
            user = result.scalar_one_or_none()
            user.refresh_token = token
            await session.commit()
            return user
