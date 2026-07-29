# API REST com Flask e SQLAlchemy

Projeto desenvolvido para praticar a criação de uma API REST utilizando **Flask**, **SQLAlchemy** e **SQLite**.

## Tecnologias

- Python
- Flask
- SQLAlchemy
- SQLite

## Funcionalidades

- Cadastro de usuários
- Cadastro de posts
- Listagem de usuários e posts
- Busca de usuários por ID e username
- Busca de posts por ID e título

## Como executar

Clone o repositório:

```bash
git clone https://github.com/GabrielRogerDelano/API-SqlAlchemys.git
```

Entre na pasta do projeto:

```bash
cd API-SqlAlchemys
```

Instale as dependências:

```bash
pip install -r requirements.txt
```

Execute a aplicação:

```bash
python api.py
```

A API ficará disponível em:

```
http://127.0.0.1:5000
```

## Endpoints

### Usuários

- `GET /usuarios`
- `GET /usuario/<id>`
- `GET /usuarios?username=nome`
- `POST /new-user`

### Posts

- `GET /posts`
- `GET /posts/<id>`
- `GET /posts?search=titulo`
- `POST /new-post`

## Objetivo

Praticar conceitos de desenvolvimento backend, criação de APIs REST, utilização do SQLAlchemy ORM e manipulação de banco de dados com SQLite.

---

Desenvolvido por **Gabriel Roger Delano**.
