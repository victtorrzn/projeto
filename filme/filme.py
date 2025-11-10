class Filme:
    def __init__(self, filme, categoria):
        self.nome_filme = filme
        self.categoria = categoria
        self.__classificacao = ("L", "10", "12", "14", "16", "18")
        self.sala = None
        self.poltrona = None
        self.valor = None
        self.horario = None
        self.__ingressos = []

    @property
    def ingressos(self):
        return self.__ingressos

    @ingressos.setter
    def ingressos(self, lista):
        self.__ingressos = lista

    def registrar_ingresso(self, ingresso):
        self.__ingressos.append(ingresso)

    @property
    def filme(self):
        return self.nome_filme

    @property
    def categoria(self):
        return self.__categoria

    @property
    def classificacao(self):
        return self.__classificacao

    @filme.setter
    def filme(self, filme):
        self.nome_filme = filme

    @categoria.setter
    def categoria(self, categoria):
        self.__categoria = categoria

    @classificacao.setter
    def classificacao(self, classificacao):
        if classificacao in self.__classificacao:
            self.__classificacao = classificacao
        else:
            print('Classificação inválida. Use: L, 10, 12, 14, 16, 18')