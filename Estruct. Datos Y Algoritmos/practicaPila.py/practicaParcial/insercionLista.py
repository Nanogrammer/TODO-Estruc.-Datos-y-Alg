import numpy as np
class Lista:
    maximo = 5
    tope: object
    lista = np.array
    primero: object
    contador: int

    
    def __init__(self) -> None:
        self.tope = 0
        self.lista = np.full(self.maximo, None)
        self.primero = None
        self.contador= 0
    
    def insertar(self,elem):
        
        if self.tope < self.maximo:

                if self.lista[0] == None: ## en cabeza
                    
                    self.lista[0] = elem
                    self.tope +=1
                    
                else:
                    aux = None
                    
                    while elem < self.lista[self.contador] and self.contador < self.tope:
                        
                            aux = self.lista[self.contador]
                            self.lista[self.contador] = elem

                            if self.lista[self.contador+1] == None:
                                self.lista[self.contador+1] = aux
                                self.tope+=1
                            else:
                                while self.lista[self.contador+1] != None:
                                        aux2 = self.lista[self.contador+1]
                                        self.lista[self.contador+1] = aux
                                        self.contador+=1
                                self.tope+=1

    def mostrar(self):
        for i in range(len(self.lista)):
             print(self.lista[i])

if __name__ == "__main__":
    lista = Lista()

    op = 0
    
    while op != "7":
            
        print("1. insertar numero")
        print("2. mostrar")
        op = input("ingrese un numero\n")
        if op == "1": 

            elem = input("ingrese un numero puto\n")
            lista.insertar(elem)
        elif op =="2":
            lista.mostrar()
        else:
             op = input("Ingrese de nuevo bien puto\n")



                                
