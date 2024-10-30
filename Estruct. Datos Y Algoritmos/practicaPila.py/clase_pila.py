import numpy as np
class Pila:
    __pila: np.array
    __tope: int
    __cant= 5

    def __init__(self) -> None:
        self.__pila = np.full(self.__cant,None)
        self.__tope= -1

    def insertar(self,x):
        y = self.llena()
        
        if y !=1:
            self.__tope +=1
            self.__pila[self.__tope] = x
            print(f"elementos insertado en el indice: {self.__tope+1}")
        return self.__pila[self.__tope]
            

    def suprimir(self):   
        x=self.vacio()
        x = self.__pila[self.__tope]
        if x!=1:
            print (f"Elemento suprimido: {self.__pila[self.__tope]} del indice {self.__tope}")
            self.__pila[self.__tope] = None
            self.__tope = self.__tope -1
        else:
            print("elemento no pudo ser SUPRIMIDO")
        return x
                
    def vacio(self):
        result=-1
        if self.__tope == -1:
            print("||La pila está vacia||")
            result = 1
        else:
            result = 0
        return result

    def llena(self):
        if self.__tope == self.__cant-1:
            print("La Lista está LLena\n")
            result = 1
        else:
            result = 0
        return int(result)
    
    def mostrarPila(self):
        print("Estado de la pila:", self.__pila)
            
    def getpila(self):
        return self.__pila

def factorial(n):
    resultado = 1
    pila1 = Pila()
    
    
    while n > 0:
        pila1.getpila().insertar(int(n))
        n-=1
    
    while pila1.getpila().vacio()!=1:
        actual = pila1.getpila().suprimir()
        resultado *= actual
        
    print(f"EL FACTORIAL ES: {resultado}")

        
    