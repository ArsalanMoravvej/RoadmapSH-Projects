from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.sql.expression import text
from sqlalchemy.sql.sqltypes import TIMESTAMP

from .database import Base

class Task(Base):
    __tablename__ = "tasks"

    id          = Column(Integer, primary_key=True, nullable=False)
    title       = Column(String, nullable=False)
    description = Column(String, nullable=False)
    status      = Column(Integer, nullable=False, server_default="1")
    priority    = Column(Integer, nullable=False, server_default="5")
    created_at  = Column(TIMESTAMP(timezone=True),
                        nullable=False, server_default = text('now()'))
    owner_id    = Column(Integer, ForeignKey("users.id", 
                                          ondelete="CASCADE"), nullable=False)

    owner = relationship("User")


class User(Base):
    __tablename__ = "users"

    id         = Column(Integer, primary_key=True, nullable=False)
    name       = Column(String, nullable=False)
    email      = Column(String, nullable=False, unique=True)
    password   = Column(String, nullable=False)
    created_at = Column(TIMESTAMP(timezone=True),
                        nullable=False, server_default = text('now()'))