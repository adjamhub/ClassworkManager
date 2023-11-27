from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "Hello, World!"

@app.route("/nuovapagina/")
def nuovapagina():
    s = "<h1>Ciao</h1>"
    s += "Sei sull'altra pagina..."
    return s

if __name__ == "__main__":
    app.run(host = "127.0.0.1", port = 5000, debug = True)
