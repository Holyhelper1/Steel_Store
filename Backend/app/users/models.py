from app.database import Base
from sqlalchemy import Column, String, UUID
import uuid

class User(Base):
    __tablename__ = 'users'
    id = Column(UUID(as_uuid=True), primary_key=True, nullable=False, index=True, default=uuid.uuid4())
    email = Column(String, nullable=False)
    hashed_password = Column(String, nullable=False)
    refresh_token = Column(String)