from models import Usuario, Jogo

SQL_USUARIO_POR_NOME = 'SELECT nome, email, senha, id_user from usuario where email = %s'
SQL_BUSCA_JOGOS = 'SELECT codigo, tipo, nome, estado, detalhes, fabricante, ano, acessórios, preco from colecao'
SQL_ATUALIZA_USUARIO = 'UPDATE usuario SET nome=%s, email=%s, senha=%s where id_user = %s'
SQL_CRIA_USUARIO = 'INSERT into usuario (nome, email, senha) values (%s, %s, %s)'


class JogoDao:
    def __init__(self, db):
        self.__db = db

    def listar(self):
        cursor = self.__db.connection.cursor()
        cursor.execute(SQL_BUSCA_JOGOS)
        jogos = traduz_jogos(cursor.fetchall())
        return jogos


class UsuarioDao:
    def __init__(self, db):
        self.__db = db

    def buscar_por_nome(self, nome):
        cursor = self.__db.connection.cursor()
        cursor.execute(SQL_USUARIO_POR_NOME, (nome,))
        dados = cursor.fetchone()
        usuario = traduz_usuario(dados) if dados else None
        return usuario

    def salvar(self, usuario):
        cursor = self.__db.connection.cursor()

        if (usuario.id):
            cursor.execute(SQL_ATUALIZA_USUARIO, (usuario.nome, usuario.email, usuario.senha, usuario.id))
        else:
            cursor.execute(SQL_CRIA_USUARIO, (usuario.nome, usuario.email, usuario.senha))
            usuario.id = cursor.lastrowid
        self.__db.connection.commit()
        return usuario


def traduz_jogos(jogos):
    def cria_jogo_com_tupla(tupla):
        return Jogo(tupla[1], tupla[2], tupla[3], tupla[4], tupla[5], tupla[6], tupla[7], tupla[8], id=tupla[0])
    return list(map(cria_jogo_com_tupla, jogos))


def traduz_usuario(tupla):
    return Usuario(tupla[0], tupla[1], tupla[2], tupla[3])
