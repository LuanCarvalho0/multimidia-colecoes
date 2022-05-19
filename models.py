class Jogo:
    def __init__(self, tipo, nome, estado, detalhes, fabricante, ano, acessorios, preco, id=None):
        self.tipo = tipo
        self.codigo = id
        self.nome = nome
        self.estado = estado
        self.detalhes = detalhes
        self. fabricante = fabricante
        self.ano = ano
        self.acessorios = acessorios
        self.preco = preco


class Usuario:
    def __init__(self, nome, email, senha, id=None):
        self.id = id
        self.nome = nome
        self.email = email
        self.senha = senha
