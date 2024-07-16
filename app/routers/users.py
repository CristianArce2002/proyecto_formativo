from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from schemas.user import UserCreate
from crud.users import create_user_sql
from db.database import get_db

router = APIRouter()

@router.post("/create")
async def insert_user(user: UserCreate, db: Session = Depends(get_db)):
    respuesta = create_user_sql(db, user)

    if respuesta: 
        return {"mensaje":"Usuario creado correctamente"}