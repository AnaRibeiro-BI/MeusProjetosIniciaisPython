from app import app
from flask import render_template
@app.route('/')
@app.route('/index')
def index():
    nome = "turma 3"
    return render_template("index.html")
