from sqlalchemy import Column, Integer, String, Date
from sqlalchemy.orm import  relationship
from db import Base

class Usuario(Base):
    __tablename__ = "usuarios"

    id = Column(Integer, autoincrement=True, primary_key=True)
    username = Column(String(40), unique=True, nullable=False)
    email = Column(String, unique=True, nullable=False)
    data_nasc = Column(Date, nullable=False) #armazena como 'YYYY-MM-DD'

    posts = relationship("Post", back_populates="usuario")

    def __init__(self, username, email, data_nasc):
        self.username = username
        self.email = email
        self.data_nasc = data_nasc

    def to_dict(self):
        return {
            "id": self.id,
            "nome": self.username,
            "email": self.email,
            "data_nasc": self.data_nasc.isoformat()
        }