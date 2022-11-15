class Transition:
    def __init__(self, id, entrada ,saida ):
        self.id = id # identificador da transição
        self.entrada = entrada # entradas da transição
        self.saida = saida # saidas da transição
    habilitado = False # habilitada ou não
        
    def __str__(self):
        if self.habilitado:
            return f"(t{self.id} = Habilitada) \nTransição {self.id} com : \n  Entrada(s) em {self.entrada}, \n  Saida(s) em {self.saida}"
        else:
            return f"(t{self.id} = Desabilitada) \nTransição {self.id} com: \n  Entrada(s) em {self.entrada}, \n  Saida(s) {self.saida} "
    def atualizarStatus(self) : 
        if self.entrada.fichas >= 1:
            self.habilitado = True
        else :
            self.habilitado = False
        
    def acionar(self):
        self.atualizarStatus()
        if self.habilitado :
            self.entrada.retirarFicha(1) # considerando arco de entrada de peso 1
            self.saida.adicionarFicha(1) # considerando arco de saida de peso 1            
        else :
            print("Transição não habilitada")
        
        