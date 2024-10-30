import random
import string

class Nodo:

    frecuencia: int
    caracter: str
    izquierda: object
    derecha: object



    def __init__(self, frec, car):
        self.frecuencia = frec
        self.caracter = car
        self.izquierda = None
        self.derecha = None

    def __str__(self):
        return f"Frecuencia: {self.frecuencia}\t\tCaracter:{self.caracter}"
    

class Arbol:    
    raiz: Nodo
    

    def __init__(self) -> None:    
        self.raiz = None

    def insertar(self,X,L):
        nuevo = Nodo(X,L)
        if self.raiz == None:
            self.raiz = nuevo
        else:
            self.insertarRec(self.raiz,nuevo)
    
    def insertarRec(self,raiz,nuevo):
        pass
    





    def Huffman(self):
        pass

   

if __name__ == "__main__":
    Arb = Arbol()
    L = []
    Letritas = ["a","b","c","d","e","f","g","h","i","j","k","m"]
    for i in range(10):
        frecue = random.randint(1,25)
        letras_aleatorias = Letritas[i]
        nodoX = Nodo(frecue, letras_aleatorias)
        L.append(nodoX)
    for i in L:
        print(i)



    


    
