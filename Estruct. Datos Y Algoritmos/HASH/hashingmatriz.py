import numpy as np
class Hash:
    matriz: np.array
    n = 10
    m = 10
    maximo = n * m

    def __init__(self):
        self.matriz = np.zeros(self.n,self.m)

    def insertar(self,valor):
        pass
    
    def hashDiv(self,valor):
    
        indice = valor % self.maximo
        return indice

    def PoliticaX(self):
        pass
if __name__ == "__main__":
    pass
    

         