from flask import Flask
from flask import url_for
from flask import request

app = Flask(__name__)

@app.route("/")
def pagina_inicial():
    return f"<h1>Página inicial.</h1>"

@app.route("/ola_mundo")
def ola_mundo():
    return "<h1>Olá Mundo!</h1>"

@app.route("/bem_vindo/<usuario>/<int:idade>/<float:altura>")
def bem_vindo(usuario, idade, altura):
    print(f"Tipo da variável usuário: {type(usuario)}")
    print(f"Tipo da variável idade: {type(idade)}")
    print(f"Tipo da variável altura: {type(altura)}")
    return f"<h1>Seja bem-vindo usuário {usuario}, {idade} anos e {altura} de altura.</h1>"

@app.route("/projects/")
def projects():
    return "<h1>The project page.</h1>"

@app.route("/about", methods=["GET", "POST"])
def about():
    if request.method == "GET":
        return "<h1>This is a GET.</h1>"
    else:
        return "<h1>This is a POST.</h1>"

with app.test_request_context():
    print(url_for("ola_mundo"))
    print(url_for("projects"))
    print(url_for("about", next="/"))
    print(url_for("bem_vindo", usuario="Ian", idade=24, altura=1.78))