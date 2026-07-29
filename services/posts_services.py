from flask import request
from db import Session
from models.post import Post

def listar_posts():
    pesquisa = request.args.get("search")

    with Session() as session:
        if pesquisa:
            posts = session.query(Post).filter(
                Post.titulo.like(f"%{pesquisa}%")
            )
        else:
            posts = session.query(Post).all()
        
        return [Post.to_dict(post) for post in posts], 200

def buscar_posts_por_usuario(user):
    with Session() as session:
        posts = session.query(Post).filter_by(usuario_id=user).all()
        
        return [Post.to_dict(post) for post in posts], 200
    
def novo_post():
    dados = request.json

    titulo = dados.get("titulo")
    userId = dados.get("userID")

    with Session() as session:
        post = Post(titulo, userId)

        session.add(post)
        session.commit()

        return {
            "Mensage": "Post criado com sucesso",
            "Post": post.to_dict()
        }, 201