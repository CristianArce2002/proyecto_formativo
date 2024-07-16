from fastapi import FastAPI
from db.database import test_db_connection
from routers import users
from routers import roles

app = FastAPI()

@app.on_event("startup")
def on_startup():
    test_db_connection()

app.include_router(users.router, prefix="/users", tags=["users"])
app.include_router(roles.router, prefix="/roles", tags=["roles"])
