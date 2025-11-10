class Pessoa:
    def __init__(self,nome, usuario,senha,idade):
        self.__nome = nome
        self.__usuario = usuario
        self.__senha = senha
        self.__idade = idade

    @property
    def nome(self):
        return self.__nome

    @property
    def usuario(self):
        return self.__usuario

    @property
    def senha(self):
        return self.__senha

    @property
    def idade(self):
        return self.__idade

    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    @usuario.setter
    def usuario(self, usuario):
        self.__usuario = usuario

    @senha.setter
    def senha(self, senha):
        self.__senha = senha

    @idade.setter
    def idade(self, idade):
        self.__idade = idade

    def funcao(self):
        return "Pessoa Comum"