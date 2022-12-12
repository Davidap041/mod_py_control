# import pandas as pd
import json
# JSON file
f = open ('rp.json', "r")
  
# Reading from file
data = json.loads(f.read())
  
# Iterating through the json
# list
cpn_net = data['workspaceElements']['cpnet']
cpn_place = cpn_net[0]['page'][0]['place']
cpn_transition = cpn_net[0]['page'][0]['trans']
print(cpn_transition)

# Closing file
f.close()

''' Extrair lugares do CPN Tools '''
index = 0
lugares = []
for place in cpn_place:
    text = place['text'][0]
    # print(text)
    lugares.append(f'    Place({index},0,\'{text}\'),')
    index += 1

''' Extrair Transicoes do CPN Tools'''
index = 0
transicoes = []
for trans in cpn_transition:
    text = trans
    print(text,end='\n')
    # lugares.append(f'    Place({index},0,\'{text}\'),')
    index += 1

'''Salvar Lugares'''
# print(lugares)
data = '\n'.join(lugares)
data = 'lugares = [\n' + data +'\n]'
# print(data)
f = open("data/cpn_lugares.py", "w")
f.write(data)
f.close()