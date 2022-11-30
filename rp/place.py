# Modelagem de um lugar
class Place:
    # atributos
    def __init__(self, id: int, fichas: int, nome: str):
        self.id = id  # id : numero do lugar
        self.nome = nome  # nome : nome do lugar
        self.fichas = fichas  # fichas : quantidade de fichas no local

    def __str__(self):
        return f'p{self.id} = {self.fichas} {self.nome} : com {self.fichas} fichas'

    # metods
    def retirarFicha(self, n:int ):
        self.fichas = self.fichas - n

    def adicionarFicha(self, n:int ):
        self.fichas = self.fichas + n

# Modelagem dos lugares
