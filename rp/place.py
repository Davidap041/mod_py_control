from rp.sensores import *
from rp.atuadores import *

''' Inicializar Sensores '''
sensores = Sensores()

''' Modelagem de um lugar em rede de petri '''


class Place:
    # atributos
    def __init__(self, id: int, fichas: int, nome: str):
        self.id = id  # id : numero do lugar
        self.nome = nome  # nome : nome do lugar
        self.fichas = fichas  # fichas : quantidade de fichas no local

    def __str__(self):
        return f'p{self.id} = {self.fichas} {self.nome} : com {self.fichas} fichas'

    # metods
    def retirarFicha(self, n: int):
        self.fichas = self.fichas - n

    def adicionarFicha(self, n: int):
        self.fichas = self.fichas + n


''' Modelagem de uma transicao na rede de petri'''


class Transition:
    def __init__(self, id: int, entradas: list[Place], saidas: list[Place]):
        self.id = id  # identificador da transição
        self.entradas = entradas  # entradas da transição
        self.saidas = saidas  # saidas da transição
        self.habilitado = False  # habilitada ou não

    def __str__(self):
        if self.habilitado:
            return f"(t{self.id} = Habilitada) \nTransição {self.id} com : \n  Entrada(s) em {self.entradas}, \n  Saida(s) em {self.saidas}"
        else:
            return f"(t{self.id} = Desabilitada) \nTransição {self.id} com: \n  Entrada(s) em {self.entradas}, \n  Saida(s) {self.saidas} "

    def atualizarStatus(self):
        count = 0
        for entrada in self.entradas:
            if entrada.fichas >= 1:
                count = count + 1

        if count == len(self.entradas):
            self.habilitado = True
        else:
            self.habilitado = False

    def acionar(self):
        self.atualizarStatus()
        if self.habilitado:
            # considerando arco de entrada de peso 1
            for entrada in self.entradas:
                entrada.retirarFicha(1)

            # considerando arco de saida de peso 1
            for saida in self.saidas:
                saida.adicionarFicha(1)

        else:
            print("Transição não habilitada")


''' Classe de asociao entre os lugares e os sensores e atuadores'''


class Controle:
    def __init__(self, index: int, dispositivo_associado, tipo: str, lugar_associado: Place):
        self.index = index
        self.dispositivo_associado = dispositivo_associado
        self.tipo = tipo
        self.lugar_associado = lugar_associado

    def atualizarElemento(self):
        if self.dispositivo_associado.lerSinal():
            self.lugar_associado.adicionarFicha(1)
        else:
            self.lugar_associado.retirarFicha(1)


''' Definição dos lugares da Rede de Petri rp '''

# Lugares da rede rp
p = [
    Place(0, 0, 'lidsConveyor'),
    Place(1, 1, 'Lids Emitter'),
    Place(2, 0, 'basesConveyor'),
    Place(3, 0, 'Bases Emitter'),
    Place(4, 0, 'lidAtPlace'),
    Place(5, 0, 'clampLid'),
    Place(6, 0, 'lidClamped'),
    Place(7, 0, 'moveZ'),
    Place(8, 0, 'movingZ'),
    Place(9, 0, 'grab'),
    Place(10, 0, 'moveX'),
    Place(11, 0, 'movingX'),
    Place(12, 1, 'bf1'),
    Place(13, 0, 'Base at place'),
    Place(14, 0, 'bfb1'),
    Place(15, 0, 'Clamp base'),
    Place(16, 0, 'Base clamped'),
    Place(17, 0, 'bfb2'),
    Place(18, 0, 'bf3'),
    Place(19, 0, 'p19'),
    Place(20, 0, 'p20'),
    Place(21, 0, 'p21'),
    Place(22, 0, 'Pos. raise (bases)'),
    Place(23, 0, 'p23'),
    Place(24, 0, 'Pos limit (bases)'),
    Place(25, 0, 'p25'),
]


'''  Definição das trasições da Rede de Petri rp '''

t = [
    Transition(0,
               [p[1]],
               [p[0]]),
    Transition(1,
               [p[0], p[12]],
               [p[0], p[4]]),
    Transition(2,
               [p[4], p[0]],
               [p[4], p[5]]),
    Transition(3,
               [p[5]],
               [p[6]]),
    Transition(4,
               [p[6]],
               [p[7], p[8]]),
    Transition(5,
               [p[7], p[8], p[18]],
               [p[7], p[9]]),
    Transition(6,
               [p[7], p[9], p[4]],
               [p[9], p[8]]),
    Transition(7,
               [p[8], p[9], p[18]],
               [p[9], p[10], p[11]]),
    Transition(8,
               [p[10], p[11]],
               [p[10], p[7], p[8]]),
    Transition(9,
               [p[7], p[9],  p[10], p[8]],
               [p[7], p[10], p[19]]),
    Transition(10,
               [p[19], p[7]],
               [p[8], p[20]]),
    Transition(11,
               [p[8], p[20]],
               [p[12]]),
    Transition(12,
               [p[21], p[23]],
               [p[22]]),
    Transition(13,
               [p[22], p[25]],
               [p[22], p[24]]),
    Transition(14,
               [p[24]],
               [p[25]]),
    Transition(15,
               [p[3]],
               [p[25]]),
    Transition(16,
               [p[25], p[14]],
               [p[25], p[13]]),
    Transition(17,
               [p[13], p[25]],
               [p[15]]),
    Transition(18,
               [p[15], p[17]],
               [p[16]]),
    Transition(19,
               [p[15], p[16]],
               [p[23]]),
]

''' Associação de Controle e Memorias dos Lugares '''

elementos = [
    Controle(0, lista_atuadores[3], 'Atuador', p[0]),      # Lids Conveyor
    Controle(1, lista_atuadores[4], 'Atuador', p[1]),      # Lids Emitter
    Controle(2, lista_atuadores[5], 'Atuador', p[2]),      # Bases Conveyor
    Controle(3, lista_atuadores[7], 'Atuador', p[3]),      # Bases Emmiter
    Controle(4, lista_sensores[6], 'Sensor', p[4]),        # Lid at Place
    Controle(5, lista_atuadores[8], 'Atuador', p[5]),      # Clamp Lid
    Controle(6, lista_sensores[7], 'Sensor', p[6]),        # Lid Clamped
    Controle(7, lista_atuadores[1], 'Sensor', p[7]),       # Move Z
    Controle(8, lista_sensores[4], 'Sensor', p[8]),        # Moving Z
    Controle(9, lista_atuadores[0], 'Sensor', p[9]),       # Grab
    Controle(10, lista_atuadores[2], 'Sensor', p[10]),     # Move X
    Controle(11, lista_sensores[5], 'Sensor', p[11]),      # Moving X
    Controle(12, '', 'Memoria', p[12]),                    # bf1
    Controle(13, lista_sensores[12], 'Sensor', p[13]),     # Base at Place
    Controle(14, '', 'Memoria', p[14]),                    # bfb1
    Controle(15, lista_atuadores[10], 'Atuador', p[15]),   # Clamp Base
    Controle(16, lista_sensores[9], 'Sensor', p[16]),      # Base Clamped
    Controle(17, '', 'Memoria', p[17]),                    # bfb2
    Controle(18, '', 'Memoria', p[18]),                    # bf3
    Controle(19, '', 'Memoria', p[19]),                    # p19
    Controle(20, '', 'Memoria', p[20]),                    # p20
    Controle(21, '', 'Memoria', p[21]),                    # p21
    Controle(22, lista_atuadores[11], 'Atuador', p[22]),   # Pos. Raise (Base)
    Controle(23, '', 'Memoria', p[23]),                    # p23
    Controle(24, lista_atuadores[9], ' Atuador ', p[23]),  # Pos. Rais (Lids)
    Controle(25, '', 'Memoria', p[25]),                    # p25
]


# Modelagem dos lugares
class Lugares:
    lugares = p
    # controle = elementos
    # atributos

    def __str__(self) -> str:
        for lugar in self.lugares:
            print(lugar)
        return f'\n'

    def printLugares(self) -> str:
        for lugar in self.lugares:
            print(lugar)
        return f'\n'

    def atualizarLugares(self, vetor):
        # Atualizar estado dos sensores na classe Sensor
        sensores.atualizarSensores(vetor)
        # Atualizar quantidade de fichas de acordo com o tipo
        for item in elementos:
            if item.tipo == 'Sensor':
                item.atualizarElemento()
