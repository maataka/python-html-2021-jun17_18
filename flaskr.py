import sqlite3
from flask import Flask, g, render_template, request
# g é variavel global do flask

# Configurações

# end do arq DB
DATABASE = './flaskr.db'
SECRET_KEY = "pudim"
USERNAME = 'admin'
PASSWORD = 'admin'

# Aplicação

# fç pra conectar db
app = Flask(__name__)
app.config.from_object(__name__)

def connect_db():
    return sqlite3.connect(DATABASE)


# criação de rota
@app.before_request
def before():
    g.db = connect_db()

@app.teardown_request
def after(exception):
    g.db.close()


@app.route('/')
def index():
    sql = 'SELECT titulo, texto from entradas ORDER BY id DESC'
    cur = g.db.execute(sql)
    entradas = [dict(titulo=titulo, texto=texto) for titulo, texto in cur.fetchall()]

   # entradas = [{'titulo': 'O primeiro Post',
   #              'texto': 'texto do post'},
   #             {'titulo': 'Segundo Post',
   #              'texto': 'Texto do segundo post'},
   #              {'titulo': 'terceiro Post',
   #              'texto': 'terceiro post'}
    return render_template('index.html', entradas=entradas)

@app.route('/inserir', methods=['POST'])
def inserir_post():
    SQL='Insert into entradas(titulo, texto) values (?,?)'
    g.db.execute(sql,[request.form['titulo'], request.form['texto']] )
    g.db.commit()
    return render_template('index.html')