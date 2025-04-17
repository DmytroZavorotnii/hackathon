from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from sqlalchemy import String, Integer, Text, DateTime, func
from typing import Optional
import os

DATABASE_URL = "postgresql+asyncpg://postgres:postgres@localhost:5437/telegram_bot_db"

engine = create_async_engine(DATABASE_URL, echo=True)
async_session = async_sessionmaker(engine, expire_on_commit=False)

class Base(DeclarativeBase):
    pass

class UserMessage(Base):
    __tablename__ = "user_messages"

    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column()
    message_text: Mapped[str] = mapped_column(Text)
    timestamp: Mapped[Optional[DateTime]] = mapped_column(DateTime(timezone=True), server_default=func.now())
