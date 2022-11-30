import time
from pyModbusTCP.client import ModbusClient

''' Inicializar Cliente Modbus '''
c = ModbusClient(host='192.168.1.131', port=502, auto_open=True, debug=False)

''' main loop '''
i = 1
bit = True
while True:
    print(f'\n -- Step : {i} ')
    
    '''Test Write Single Coils'''
    for ad in range(20,35):
        is_ok = c.write_single_coil(ad, bit)
        if is_ok:
            print('coil #%s: write to %s' % (ad, bit))
        else:
            print('coil #%s: unable to write %s' % (ad, bit))
        # time.sleep(0.5)

    '''Test Write Multiple Coils'''
    ad = 20
    is_ok = c.write_multiple_coils(ad, [bit, bit, bit, bit,bit])
    print(is_ok)
    
    # sleep 2s before next polling
    bit = not bit
    i +=1
    time.sleep(0.5)


    