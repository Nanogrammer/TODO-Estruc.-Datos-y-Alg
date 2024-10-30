import numpy as np
## ultimo en entrar primero en salir
## ultimo en entrar primero en salir
## ---------------------SUPRIMIR COMPLICADO-----------------------
## ---------------------SUPRIMIR COMPLICADO-----------------------

class Pila:
    
     
#----------------------------------------------#
#-----------------TAD PILA---------------------#
    ultimo: object
    tope: int
    maximo= 5
    pilita : np.array
#-----------------------------------------------#
#-----------------------------------------------#


    def __init__(self):

        self.tope = 0
        self.ultimo = None
        self.pilita = np.full(self.maximo,None)

    def insertar(self,elem):

        if self.lleno()!= True:
            if self.tope < self.maximo:
                self.pilita[self.tope] = elem
                self.ultimo = self.pilita[self.tope]
                self.tope+=1

    def lleno(self):
        pass



if __name__ == "__main__":
    pila = Pila()
    pila.insertar(elem=3)


    