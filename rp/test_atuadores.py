from atuadores import *

'''Inicializar atuadores'''
valor_inicial = [False]*20
atuadores = Atuadores(valor_inicial)

print(atuadores.lerAtuadores())

'''Acionar atuador'''
print('\n')
atuadores.acionarAtuador(0,True)

# print(atuadores.lerAtuadores())

'''Acionar atuadores '''
sinais = [True, False, True, True, False, 
          True, False, True, False, False, 
          False, False, False, False, False,
          False, False, False, False, False]
# ler atuadores na classe
sinal_atuadores = atuadores.valorAtuadores() 
# atualizar na rede modbus
# is_ok = c.write_multiple_coils(20,sinal_atuadores)

print(atuadores.lerAtuadores())

'''Acionar Multiplos atuadores'''
atuadores.acionarAtuadores(sinais)