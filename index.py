from flask import Flask, render_template, request, redirect, session, flash, url_for
from dao import UsuarioDao, JogoDao
from flask_mysqldb import MySQL
from models import Usuario

app = Flask(__name__)
app.secret_key = 'luan'

app.config['MYSQL_HOST'] = "127.0.0.1"
app.config['MYSQL_USER'] = "root"
app.config['MYSQL_PASSWORD'] = "Carvalho19"
app.config['MYSQL_DB'] = "bancocolecoes"
app.config['MYSQL_PORT'] = 3306

db = MySQL(app)

usuario_dao = UsuarioDao(db)
jogo_dao = JogoDao(db)


@app.route('/')
def index():
    lista = jogo_dao.listar()
    return render_template('lista.html', titulo='Coleções', jogos=lista)


@app.route('/novousuario')
def novo():
    return render_template('novousuario.html', titulo='Novo Usuario')


@app.route('/novo_usuario', methods=['POST', ])
def novo_usuario():
    nome = request.form['nome']
    email = request.form['email']
    senha = request.form['senha']
    usuario = Usuario(nome, email, senha)
    usuario_dao.salvar(usuario)
    flash(' Usuario cadastrado com sucesso!')
    return redirect(url_for('index'))


@app.route('/login')
def login():
    proxima = request.args.get('proxima')
    return render_template('login.html', proxima=proxima)


@app.route('/autenticar', methods=['POST', ])
def autenticar():
    usuario = usuario_dao.buscar_por_nome(request.form['usuario'])
    if usuario:
        if request.form['senha'] == usuario.senha:
            session['usuario_logado'] = usuario.email
            flash(usuario.nome + ' logado com sucesso!')
            proxima_pagina = request.form['proxima']
            if proxima_pagina == 'None':
                return redirect(url_for('index'))
            return redirect(url_for(proxima_pagina))
    else:
        flash('Usuário não logado!')
        return redirect(url_for('login'))


@app.route('/logout')
def logout():
    session['usuario_logado'] = None
    flash('Logout efetuado com sucesso!')
    return redirect(url_for('index'))


if __name__ == "__main__":
    app.run(debug=True)
