from sqlalchemy import text
from sqlalchemy.orm import Session
from schemas.role import RoleCreate

def create_role_sql(db: Session, role: RoleCreate):
    sql_query = text(
        "INSERT INTO roles (rol_name) VALUES (:rol_name)"
    )
    params = {
        "rol_name": role.rol_name
    }
    db.execute(sql_query, params)
    db.commit()
    return True  # Retorna True si la inserción fue exitosa