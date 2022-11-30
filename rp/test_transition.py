from place import Place
from transition import Transition
p1 = Place(id=1,fichas=2,nome='Move X')
p2 = Place(id=2,fichas=2,nome='Move Y')

t1 = Transition(id=1,entrada=p1,saida=p2)
print(t1)

t1.acionar()
print(t1)

