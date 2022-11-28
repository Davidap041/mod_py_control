import time
from rp.sensores import Sensores
from pyModbusTCP.client import ModbusClient
# init modbus client
c = ModbusClient(host='10.109.60.127', port=502, auto_open=True, debug=False)
sensores = Sensores()
# main read loop
while True:
    # read 18 bits (= coils) at address 0, store result in coils list
    leitura_sensores = c.read_coils(0, 18)
    sensores.atualizarSensores(vetor = leitura_sensores )

    # if success display registers
    if leitura_sensores:
        print('\n')
        # sensores.lerSensores()
        print(sensores.lerSensor(5))
        is_ok = c.write_single_coil(24,True)
    else:
        print('unable to read coils')

    # sleep 2s before next polling
    time.sleep(2)


    