from fastapi import FastAPI

from .initialize import init
from .routers import admin, me, public, token

init()

app = FastAPI()

app.include_router(public.router, tags=["public"])
app.include_router(token.router, tags=["token"])
app.include_router(me.router, tags=["me"])
app.include_router(admin.router, tags=["admin"])
