from datetime import datetime

from app.enums.task_status import TaskStatus
from sqlalchemy import Column, DateTime, Integer, String, func, ForeignKey, Text, UniqueConstraint
from app.config.database import Base
from sqlalchemy.orm import mapped_column, relationship


class Task(Base):
    __tablename__ = 'tasks'
    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = mapped_column(ForeignKey('users.id'))
    title = Column(String(150), index=True)
    description = Column(Text, nullable=True, default=None)
    status = Column(String(255), default=TaskStatus.TO_DO, nullable=False)
    updated_at = Column(DateTime, nullable=True, default=None, onupdate=datetime.now)
    created_at = Column(DateTime, nullable=False, server_default=func.now())

    __table_args__ = (UniqueConstraint('user_id', 'title', name='unique_task'),)

    user = relationship('User', back_populates='tasks')
