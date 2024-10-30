import numpy as np
class Cola:
    maximo = 5
    primer: int
    ultimo: int
    cantidad: int
    Lista: np.array

    def __init__(self) -> None:
        self.primer=0
        self.ultimo=0
        self.cantidad=0
        self.Lista = np.full(5, None)
    

    def vacio(self):
        result = None
        if self.cantidad == 0:
            result = True
        else:
            result = False
        return result
    
    def lleno(self):
        result = None
        if self.cantidad < self.maximo:
            result =  False
        else:
            result = True
        return result
    

    def suprimir(self):
        if self.vacio() is False:
            x = self.Lista[self.primer]
            self.Lista[self.primer] = None
            self.primer = (self.primer + 1) % self.maximo
            self.cantidad -= 1
            return x
        else:
            print("Cola Vacia no se puede suprimir")
    
    def insertar(self,x):
        if self.lleno() is False:
            self.Lista[self.ultimo] = x
            self.ultimo = (self.ultimo +1) % self.maximo
            self.cantidad += 1
            return x
        else:
            print(" COla LLena no se puede insertar")

    def mostrar(self):
        print("----------------------ITEMS DE LA LISTA---------------------------")
        for item in self.Lista:
            print(item)
        print("------------------------------------------------------------------")

if __name__ == "__main__":
    colita = Cola()
    op = 0

    while op != "7":
        print("1. insertar")
        print("2. suprimir")
        print("3. recorrerr")
        op = input("ingrese una opcion\n")

        if op == "1":
            y = int(input("ingrese un numero\n"))
            colita.insertar(y)
        elif op == "2":
            colita.suprimir()
        elif op == "3":
            colita.mostrar()

        else:
            op = input("ingrese una opcion\n")
        