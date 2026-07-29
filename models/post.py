from datetime import datetime as dt
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from db import Base

class Post(Base):
    __tablename__ = "posts"

    id = Column(Integer, autoincrement=True, primary_key=True)
    titulo = Column(String, nullable=False)

    usuario_id = Column(Integer, ForeignKey("usuarios.id"))
    usuario = relationship("Usuario", back_populates="posts")
    data_postagem = Column(DateTime)

    def __init__(self, titulo, usuario_id):

        self.titulo = titulo
        self.usuario_id = usuario_id
        self.data_postagem = dt.today()

    def to_dict(self):
        return {
            "id": self.id,
            "titulo": self.titulo,
            "usuario": self.usuario.username,
            "data_postagem": self.data_postagem
        }
    
