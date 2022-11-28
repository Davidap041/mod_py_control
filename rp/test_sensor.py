from sensores import *

# inicializar um sensor
# s0 = Sensor(0,'mySensor',False)
# print(s0)

# atualizar o sinal do sensor
# s0.atualizarSensor(True)
# print(s0)

# inicilizar o conjunto de sensores padrão
sensores = Sensores()
# print(sensores)

print(sensores.lerSensor(5))
