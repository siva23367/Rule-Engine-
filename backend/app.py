import os
from contextlib import asynccontextmanager

import uvicorn
from aiohttp import ClientSession
from arq import create_pool
from Ast.routes import router as AstRouter


from fastapi import Depends, FastAPI


from settings import TORTOISE_ORM
from starlette.middleware.cors import CORSMiddleware

from tortoise.contrib.fastapi import register_tortoise





app = FastAPI(title="RuleEngine")






register_tortoise(
    app,
    config=TORTOISE_ORM,
    generate_schemas=True,
    add_exception_handlers=True,
)

app.include_router(AstRouter, prefix="/ast")







@app.get("/")
async def read_root():
    return "Hi, Welcome to the RuleEngine API"

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
