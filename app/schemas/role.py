from typing import Annotated
from pydantic import BaseModel, StringConstraints

class RoleBase(BaseModel):
    rol_name: Annotated[str, StringConstraints(max_length=15)]

class RoleCreate(RoleBase):
    rol_name: Annotated[str, StringConstraints(max_length=15)]
    
class RoleResponse(RoleBase):
    rol_name: str