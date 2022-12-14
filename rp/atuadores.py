class Actuator:
    def __init__(self, index, nome, sinal) -> None:
        self.nome = nome
        self.sinal = sinal
        self.index = index

    def __str__(self) -> str:
        return f'Atuador {self.index} : {self.nome} = {self.sinal}'

    def atualizarActuator(self, sinal):
        self.sinal = sinal
    
    def lerSinal(self) -> bool:
        return True if self.sinal else False

lista_atuadores = [
    Actuator(0, 'Grab', False),
    Actuator(1, 'Move Z', False),
    Actuator(2, 'Move X', False),
    Actuator(3, 'Lids conveyor', False),
    Actuator(4, 'Lids emitter', False),
    Actuator(5, 'Bases conveyor', False),
    Actuator(6, 'Remover 1', False),
    Actuator(7, 'Bases emitter', False),
    Actuator(8, 'Clamp lid', False),
    Actuator(9, 'Pos. raise (lids)', False),
    Actuator(10, 'Clamp base', False),
    Actuator(11, 'Pos. raise (bases)', False),
    Actuator(12, 'Start light', False),
    Actuator(13, 'Reset light', False),
    Actuator(14, 'Stop light', False),
    Actuator(15, 'Remover 2', False),
    Actuator(16, 'Counter', False),
    Actuator(17, 'STAGES_LIDS', False),
    Actuator(18, 'STAGES_BASES', False),
    Actuator(19, 'STAGES_ROBOT', False),
]


class Atuadores:
    atuadores = lista_atuadores

    def __init__(self, sinais: list[bool]) -> None:
        self.vetorSinais: list[bool] = sinais

    def __str__(self) -> str:
        return f'Atuadores: {self.atuadores}'

    def atualizarAtuadores(self) -> list[bool]:
        index: int = 0
        for sinal in self.vetorSinais:
            self.atuadores[index].atualizarActuator(sinal)
            index += 1
        # print(f'{index} atuadores Atualizados')
        return (self.vetorSinais)

    def lerAtuadores(self) -> list[bool]:
        for atuador in self.atuadores:
            print(atuador)
        return self.vetorSinais
    
    def valorAtuadores(self) -> list[bool]:
        return self.vetorSinais

    def acionarAtuador(self, n: int, sinal: bool) -> None:
        self.vetorSinais[n] = sinal
        self.atualizarAtuadores()
        print(f'-> [set] :  {self.atuadores[n]}')

    def acionarAtuadores(self, sinais: list[bool]) -> None:
        self.vetorSinais = sinais
        self.atualizarAtuadores()
