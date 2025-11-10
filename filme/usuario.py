from filme.Pessoa import Pessoa
class Usuario(Pessoa):
    def __init__(self, nome, usuario, senha, tipo, idade):
        super().__init__(nome, usuario, senha, idade)
        self.__senha = senha
        self.__tipo = tipo
        self.__idade = idade
        self.filmes = []

    @property
    def historico_filmes(self):
        return self.filmes

    @historico_filmes.setter
    def historico_filmes(self, lista):
        self.filmes = lista

    def registrar_filmes(self, novo_filme):
        self.filmes.append(novo_filme)

    @property
    def tipo(self):
        return self.__tipo

    @tipo.setter
    def tipo(self, tipo):
        self.__tipo = tipo

    def funcao(self):
        if self.__tipo == "admin":
            return "administrador"
        elif self.__tipo == "usuario":
            return "usuário normal"
        else:
            return "Tipo Desconhecido"