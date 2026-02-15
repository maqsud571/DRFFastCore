# str/api/main.py
from fastapi import FastAPI
from sqlalchemy import insert, select
from database import AsyncSessionLocal, engine
from models import metadata, UserItem
from schemas.user import ItemCreate

app = FastAPI(title="UserItem API")

# DB table yaratish
@app.on_event("startup")
async def on_startup():
    async with engine.begin() as conn:
        await conn.run_sync(metadata.create_all)


@app.post("/items", response_model=dict)
async def create_item(item: ItemCreate):
    async with AsyncSessionLocal() as session:
        stmt = insert(UserItem).values(
            name=item.name,
            age=item.age
        ).returning(UserItem)
        result = await session.execute(stmt)
        await session.commit()
        return result.mappings().first()


@app.get("/items", response_model=list[dict])
async def get_items():
    async with AsyncSessionLocal() as session:
        result = await session.execute(select(UserItem))
        return result.mappings().all()
 

# # str/api/main.py
# from fastapi import FastAPI
# from sqlalchemy import insert, select
# from database import AsyncSessionLocal
# from models import UserItem
# from schemas.user import ItemCreate

# app = FastAPI(title="UserItem API")


# @app.post("/items", response_model=dict)
# async def create_item(item: ItemCreate):
#     async with AsyncSessionLocal() as session:
#         stmt = insert(UserItem).values(
#             name=item.name,
#             age=item.age
#         ).returning(UserItem)

#         result = await session.execute(stmt)
#         await session.commit()

#         return result.mappings().first()


# @app.get("/items", response_model=list[dict])
# async def get_items():
#     async with AsyncSessionLocal() as session:
#         result = await session.execute(select(UserItem))
#         return result.mappings().all()
