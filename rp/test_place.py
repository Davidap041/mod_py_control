from place import *

# exemplo de uso classe place
p1 = Place(id = 1,fichas = 3, nome='Clamp base')
print(p1)

p1.retirarFicha(1) # retirar uma ficha de p1
print(p1)

p1.adicionarFicha(2) # adicionar duas fichas no lugar p1
print(p1)

p2 = Place(id = 2, fichas= 1,nome ='Move X')
print(p2)
