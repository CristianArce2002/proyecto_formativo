from sqlalchemy import Column, String
from db.database import Base

class Role(Base):
    __tablename__ = "roles"

    role_name = Column(String, primary_key=True, index=True)

    def __repr__(self):
        return f"Role(role_name='{self.role_name}')"