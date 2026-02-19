from fastapi import FastAPI, Depends
from sqlalchemy import insert, select
from sqlalchemy.ext.asyncio import AsyncSession

from database import engine, get_db
from models import metadata, UserItem
from schemas.user import ItemCreate, ItemResponse

app = FastAPI(title="UserItem API")


# table create ONLY if not exists
@app.on_event("startup")
async def startup():
    async with engine.begin() as conn:
        await conn.run_sync(metadata.create_all)


# CREATE
@app.post("/items", response_model=ItemResponse)
async def create_item(
    item: ItemCreate,
    db: AsyncSession = Depends(get_db)
):
    stmt = insert(UserItem).values(
        name=item.name,
        age=item.age
    ).returning(UserItem)

    result = await db.execute(stmt)
    await db.commit()

    return result.mappings().first()


# READ
@app.get("/items", response_model=list[ItemResponse])
async def get_items(
    db: AsyncSession = Depends(get_db)
):
    result = await db.execute(select(UserItem))
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
