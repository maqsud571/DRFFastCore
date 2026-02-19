import asyncio
from database import engine
from models import metadata

async def init_db():
    async with engine.begin() as conn:
        await conn.run_sync(metadata.create_all)


# async def init_db():
#     async with engine.begin() as conn:
#         # Agar table bo'lmasa yaratadi
#         await conn.run_sync(metadata.create_all)

# # FastAPI ishga tushganda db ni yaratish
# import uvicorn
# from fastapi import FastAPI

# app = FastAPI()

# @app.on_event("startup")
# async def on_startup():
#     await init_db()
