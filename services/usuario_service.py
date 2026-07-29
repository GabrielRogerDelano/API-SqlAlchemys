from flask import request
from db import Session
from models.usuario import Usuario

def listar_usuarios():
    nome = request.args.get("username")
    with Session() as session:
        if nome:
            usuarios = session.query(Usuario).filter(
                Usuario.username.like(f"%{nome}%")
            ).all()
        else:
            usuarios = session.query(Usuario).all()

        return [Usuario.to_dict(usuario) for usuario in usuarios], 200
    
def busca_por_id(id):
    with Session() as session:
        usuario = session.query(Usuario).filter_by(id=id).first()
    
        if usuario is None:
            return {"Mensage": "Id invalido"}, 200
        else:
            return Usuario.to_dict(usuario), 200
        
def novo_usuario():
    dados = request.json
    nome = dados.get("nome")
    email = dados.get("email")
    data_nasc = dados.get("data_nasc")

    user = Usuario(nome, email, data_nasc)

    print(user)

    with Session() as session:
        session.add(user)
        session.commit()

        return {
            "Mensage": "usuario Cadastrado",
            "Usuario": user.to_dict()
        }, 201
        