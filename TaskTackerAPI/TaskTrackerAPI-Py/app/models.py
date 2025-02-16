from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, Index
from sqlalchemy.orm import relationship
from sqlalchemy.sql.expression import text
from sqlalchemy.sql.sqltypes import TIMESTAMP

from .database import Base

class Task(Base):
    __tablename__ = "tasks"
    __table_args__ = (Index("idx_tasks_is_deleted", "is_deleted"),)

    id               = Column(Integer, primary_key=True, nullable=False)
    title            = Column(String, nullable=False)
    description      = Column(String, nullable=False)
    status           = Column(Integer, nullable=False, server_default=text("1"))
    priority         = Column(Integer, nullable=False, server_default=text("5"))
    is_deleted       = Column(Boolean, nullable=False, server_default=text("false"))
    deleted_at       = Column(TIMESTAMP(timezone=True), nullable=True)
    last_modified_at = Column(TIMESTAMP(timezone=True), nullable=True)
    created_at       = Column(TIMESTAMP(timezone=True), nullable=False, server_default = text('now()'))
    owner_id         = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=False)

    owner = relationship("User")


class User(Base):
    __tablename__ = "users"
    __table_args__ = (Index("idx_users_is_deleted", "is_deleted"),)

    id               = Column(Integer, primary_key=True, nullable=False)
    name             = Column(String, nullable=False)
    email            = Column(String, nullable=False, unique=True)
    password         = Column(String, nullable=False)
    is_deleted       = Column(Boolean, nullable=False, server_default=text("false"))
    deleted_at       = Column(TIMESTAMP(timezone=True), nullable=True)
    last_modified_at = Column(TIMESTAMP(timezone=True), nullable=True)
    created_at       = Column(TIMESTAMP(timezone=True), nullable=False, server_default = text('now()'))