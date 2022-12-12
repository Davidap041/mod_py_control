import time
from rp.sensores import Sensores
from rp.atuadores import Atuadores
from pyModbusTCP.client import ModbusClient

''' Inicializar Cliente Modbus '''
c = ModbusClient(host='192.168.1.131', port=502, auto_open=True, debug=False)

''' Inicializar Sensores '''
sensores = Sensores()

''' Inicializar Atuadores '''
valor_inicial = [False]*20
atuadores = Atuadores(valor_inicial)

''' main loop '''
i = 1
bit = True
while True:
    print(f'\n -- Step : {i} ')
    ''' Atualização dos sensores '''
    # ler sensores modbus
    leitura_sensores = c.read_coils(0, 18)
    # atualizar na classe
    sensores.atualizarSensores(vetor = leitura_sensores ) 
    # atualizar lugares
    

    if leitura_sensores: # sucesso na leitura
        print('\n')
        sensores.lerSensores()
    else: # falha na leitura
        print('unable to read coils')
    
    if(i == 5 ):  sensores.lerSensor(5)
    
    ''' Atualização dos Atuadores '''    
    # atualizar atuador
    if i == 2 : atuadores.acionarAtuador(2,True)
    if i == 10: atuadores.acionarAtuador(5,True)
   
    ''' Acionamento do Atuadores'''
    # ler atuadores na classe
    sinal_atuadores = atuadores.valorAtuadores() 
    # atualizar na rede modbus
    is_ok = c.write_multiple_coils(20,sinal_atuadores)
    
    if is_ok: 
        print('\n')
        atuadores.lerAtuadores()
    else :
        print('unable to write coils')
       
    '''Test Write Single Coils'''
    # for ad in range(20,35):
    #     is_ok = c.write_single_coil(ad, bit)
    #     if is_ok:
    #         print('coil #%s: write to %s' % (ad, bit))
    #     else:
    #         print('coil #%s: unable to write %s' % (ad, bit))
    #     time.sleep(0.5)
    
    # bit = not bit

    '''Test Write Multiple Coils'''
    # ad = 20
    # is_ok = c.write_multiple_coils(ad, [bit, bit, bit, bit,bit])
    # print(is_ok)
    
    # bit = not bit
    
    # sleep 2s before next polling
    i +=1
    time.sleep(2)


    