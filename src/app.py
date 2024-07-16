from flask import Flask, url_for, request

app = Flask(__name__)

@app.route("/")
def pagina_inicial():
    return f"<h1>Página inicial.</h1>"

@app.route("/ola_mundo")
def ola_mundo():
    return {"message": "Olá Mundo!"}

@app.route("/bem_vindo/<usuario>/<int:idade>/<float:altura>")
def bem_vindo(usuario, idade, altura):
    return {
        "Usuário": usuario,
        "Idade": idade,
        "Altura": altura,
    }

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