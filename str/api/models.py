# str/api/models.py

from sqlalchemy import Table, Column, Integer, String, MetaData

metadata = MetaData()

UserItem = Table(
    "User_item",   # EXACT Django table name
    metadata,
    Column("id", Integer, primary_key=True, autoincrement=True),
    Column("name", String, nullable=False),
    Column("age", Integer, nullable=False),
)

