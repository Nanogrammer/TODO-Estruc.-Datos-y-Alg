import numpy as np
## ultimo en entrar primero en salir
## ultimo en entrar primero en salir
## ---------------------SUPRIMIR COMPLICADO-----------------------
## ---------------------SUPRIMIR COMPLICADO-----------------------


class Cola():

#----------------------------------------------#
#-----------------TAD PILA---------------------#
    primero: object
    tope: int
    ultimo: object
    maximo = 5
    cola = np.full(maximo,None)
#-----------------------------------------------#
#-----------------------------------------------#

    def __init__(self) -> None:

        self.tope = 0
        self.primero = None
        self.ultimo = None


    def insertar(self,elem):
        
        if self.tope < self.maximo:
            if self.primero == None:

                self.cola[self.tope] = elem
                self.tope+=1
            else:
                self.cola[self.tope] = elem
                self.tope+=1


if __name__ == "__main__":
    cola = Cola()
    cola.insertar(elem=3)


    