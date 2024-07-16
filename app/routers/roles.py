from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from schemas.role import RoleCreate
from crud.roles import create_role_sql
from db.database import get_db

router = APIRouter()

@router.post("/create")
async def insert_role(user: RoleCreate, db: Session = Depends(get_db)):
    respuesta = create_role_sql(db, user)

    if respuesta: 
        return {"mensaje":"Rol creado correctamente"}