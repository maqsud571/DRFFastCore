# str/api/models.py
from sqlalchemy import Table, Column, Integer, String, MetaData

metadata = MetaData()

UserItem = Table(
    "user_item",  # kichik harflar bilan, Postgres tavsiyasi
    metadata,
    Column("id", Integer, primary_key=True, autoincrement=True),
    Column("name", String, nullable=False),
    Column("age", Integer, nullable=False),
)
