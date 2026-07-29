from postgres_Flask.db import Base, engine
from postgres_Flask.models.usuario import Usuario
from postgres_Flask.models.post import Post

Base.metadata.create_all(bind=engine)

print("Banco criado com sucesso!")