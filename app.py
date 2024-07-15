from flask import Flask

app = Flask(__name__)

@app.route("/")
def pagina_inicial():
    return f"<h1>Página inicial.</h1>"

@app.route("/ola_mundo")
def ola_mundo():
    return "<h1>Olá Mundo!</h1>"