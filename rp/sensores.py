class Sensor:
    def __init__(self, index, nome: str, sinal: bool):
        self.nome = nome
        self.sinal = sinal
        self.index = index

    def __str__(self) -> str:
        return f'Sensor {self.index} : {self.nome}  = {self.sinal}'

    def atualizarSensor(self, sinal):
        self.sinal = sinal

    def lerSinal(self) -> bool:
        return True if self.sinal else False


lista_sensores = [
    Sensor(0, 'FACTORY I/O (Running)', False),
    Sensor(1, 'FACTORY I/O (Paused)', False),
    Sensor(2, 'FACTORY I/O (Reset)', False),
    Sensor(3, 'Item detected', False),
    Sensor(4, 'Moving Z', False),
    Sensor(5, 'Moving X', False),
    Sensor(6, 'Lid at place', False),
    Sensor(7, 'Lid clamped', False),
    Sensor(8, 'Pos. at limit (lids)', False),
    Sensor(9, 'Base clamped', False),
    Sensor(10, 'Pos. at limit (bases)', False),
    Sensor(11, 'Part leaving', False),
    Sensor(12, 'Base at place', False),
    Sensor(13, 'Start', False),
    Sensor(14, 'Reset', False),
    Sensor(15, 'Stop', False),
    Sensor(16, 'Emergency stop', False),
    Sensor(17, 'Manual', False),
    Sensor(18, 'Auto', False),
]


class Sensores:
    sensores = lista_sensores

    def __str__(self) -> str:
        return f'Sensores: {self.sensores}'

    def atualizarSensores(self, vetor):
        index = 0
        for sinal in vetor:
            self.sensores[index].atualizarSensor(sinal)
            index += 1
        return f'{index} sensores atualizados'

    def lerSensores(self):
        msg = ''
        for sensor in self.sensores:
            print(sensor)
        # msg += sensor
        # return msg

    def lerSensor(self, n):
        print(f'[read] : {self.sensores[n]}')
        return self.sensores[n].sinal
    '''
    def atualizarLugares()
    '''
