# from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
# from sqlalchemy.orm import sessionmaker
# import os

# DATABASE_URL = (
#     f"postgresql+asyncpg://{os.getenv('DB_USER')}:"
#     f"{os.getenv('DB_PASS')}@"
#     f"{os.getenv('DB_HOST')}:5432/"
#     f"{os.getenv('DB_NAME')}"
# )

# engine = create_async_engine(DATABASE_URL, echo=True)

# AsyncSessionLocal = sessionmaker(
#     engine, class_=AsyncSession, expire_on_commit=False
# )
# str/api/database.py
import os
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker

# .env dan o'qish
DB_USER = os.getenv("DB_USER")
DB_PASS = os.getenv("DB_PASS")
DB_HOST = os.getenv("DB_HOST")
DB_NAME = os.getenv("DB_NAME")

DATABASE_URL = f"postgresql+asyncpg://{DB_USER}:{DB_PASS}@{DB_HOST}:5432/{DB_NAME}"

engine = create_async_engine(DATABASE_URL, echo=True)

AsyncSessionLocal = sessionmaker(
    engine, class_=AsyncSession, expire_on_commit=False
)

