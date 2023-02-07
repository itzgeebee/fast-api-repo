from .database import Base
from sqlalchemy import TIMESTAMP, Column, String, Boolean
from sqlalchemy.sql import func
from fastapi_utils.guid_type import GUID, GUID_DEFAULT_SQLITE


class Test(Base):
    __tablename__ = 'tests'
    id = Column(GUID, primary_key=True, default=GUID_DEFAULT_SQLITE)
    name = Column(String, nullable=False)
    description = Column(String, nullable=False)
    category = Column(String, nullable=True)
    published = Column(Boolean, nullable=False, default=True)
    createdAt = Column(TIMESTAMP(timezone=True),
                       nullable=False, server_default=func.now())
    updatedAt = Column(TIMESTAMP(timezone=True),
                       default=None, onupdate=func.now())

class User(Base):
    __tablename__ = 'users'
    id = Column(GUID, primary_key=True, default=GUID_DEFAULT_SQLITE)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    email = Column(String, nullable=False)
    createdAt = Column(TIMESTAMP(timezone=True),
                       nullable=False, server_default=func.now())
    updatedAt = Column(TIMESTAMP(timezone=True),
                       default=None, onupdate=func.now())



