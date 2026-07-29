from flask import Flask
from services import usuario_service, posts_services

app = Flask(__name__)

@app.route("/", methods=["GET"])
def index():
    return "endpoints disponiveis <br>" \
    "GET /usuarios <br>" \
    "GET /usuarios?username=123<br> " \
    "GET /usuario/123 <br>" \
    "GET /posts <br>" \
    "GET /posts?search=123<br> " \
    "GET /posts/123<br> " \
    "POST /usuario?username=aaa" 

#GET
@app.route("/usuarios", methods=["GET"])
def get_Users():
    return usuario_service.listar_usuarios()

@app.route("/usuario/<id>", methods=["GET"])
def getById(id):
    return usuario_service.busca_por_id(id)
    
@app.route("/posts", methods=["GET"])
def getAllPosts():
    return posts_services.listar_posts()
    
@app.route("/posts/<user>", methods=["GET"])
def getAllPostsFromUserId(user):
    return posts_services.buscar_posts_por_usuario(user)

#POST
@app.route("/new-usuario", methods=["POST"])
def addUser():
    return usuario_service.novo_usuario()

@app.route("/new-post", methods=["POST"])
def newPost():
    return posts_services.novo_post()

app.run(debug=True)
