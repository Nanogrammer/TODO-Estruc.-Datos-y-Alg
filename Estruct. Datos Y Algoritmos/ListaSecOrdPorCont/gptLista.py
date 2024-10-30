import numpy as np
import random

class Nodo():
    fila: int
    columna: int
    valor: int
    siguiente: object

    def __init__(self,fila,columna,valor):
        self.fila = fila
        self.columna = columna
        self.valor = valor
        self.siguiente = None

class Lista():
    cabeza: object
    tope: int

    def __init__(self):
        self.cabeza = None
        
    
    def cargarMatriz(self,lista):   

        for i in range (3):
            for j in range(3):
                valor = int(random.randint(1,20))
                if valor <  10 :

                    lista[i][j] = int(valor)
                else: 
                    valor = 0
                    lista[i][j] = int(valor)
         
    
    def MostrarLista(self,lista):
        i = 0
        j = 0

        for i in range(3):
            for j in range(3):
                print(lista[i][j])
            print(f"fila: {i}")


    def cargarListaEnlazada(self,matriz,lista,filas,columnas):
        
        i = 0
        j = 0

        lista.cabeza = None
        contador = 0
        contadorPos= 0

        for i in range(filas):
            for j in range(columnas):
                if matriz[i][j] != 0:
                    nuevo = Nodo(i, j, matriz[i][j])
                    
                    if lista.cabeza == None:
                        lista.cabeza = nuevo
                        contadorPos+=1
                        contador -=1
        
                    else:
                        aux = lista.cabeza

                        while aux.siguiente != None:
                            aux = aux.siguiente
                        aux.siguiente = nuevo
                        contadorPos+=1
                else:
                    contador+=1
        print(f"Cantidad de elementos: {contadorPos}")
        print(f"espacios reducidos: {contador}")

            
                    

                
    def mostrarEnlazada(self,cabeza):
        
        aux = cabeza
        while aux != None:
            
            print(aux.fila, aux.columna, aux.valor)
            aux = aux.siguiente
            
    def ListaDefinitiva(self, cabeza1, cabeza2):
        aux1 = cabeza1
        aux2 = cabeza2
        self.cabeza = None
        repetidos = 0
        
        while aux1 is not None or aux2 is not None:
            # Manejo de la cabeza
            if self.cabeza is None:
                if aux1 is None:
                    self.cabeza = Nodo(aux2.fila, aux2.columna, aux2.valor)
                    aux2 = aux2.siguiente
                elif aux2 is None:
                    self.cabeza = Nodo(aux1.fila, aux1.columna, aux1.valor)
                    aux1 = aux1.siguiente
                else:
                    if aux1.fila == aux2.fila:
                        if aux1.columna == aux2.columna:
                            self.cabeza = Nodo(aux1.fila, aux1.columna, int(aux1.valor + aux2.valor))
                            repetidos += 1
                            aux1 = aux1.siguiente
                            aux2 = aux2.siguiente
                        elif aux1.columna < aux2.columna:
                            self.cabeza = Nodo(aux1.fila, aux1.columna, aux1.valor)
                            aux1 = aux1.siguiente
                        else:
                            self.cabeza = Nodo(aux2.fila, aux2.columna, aux2.valor)
                            aux2 = aux2.siguiente
                    elif aux1.fila < aux2.fila:
                        self.cabeza = Nodo(aux1.fila, aux1.columna, aux1.valor)
                        aux1 = aux1.siguiente
                    else:
                        self.cabeza = Nodo(aux2.fila, aux2.columna, aux2.valor)
                        aux2 = aux2.siguiente

                aux3 = self.cabeza

            else:
                while aux3.siguiente is not None:
                    aux3 = aux3.siguiente

                if aux1 is None:
                    aux3.siguiente = Nodo(aux2.fila, aux2.columna, aux2.valor)
                    aux2 = aux2.siguiente
                elif aux2 is None:
                    aux3.siguiente = Nodo(aux1.fila, aux1.columna, aux1.valor)
                    aux1 = aux1.siguiente
                else:
                    if aux1.fila == aux2.fila:
                        if aux1.columna == aux2.columna:
                            aux3.siguiente = Nodo(aux1.fila, aux1.columna, int(aux1.valor + aux2.valor))
                            aux1 = aux1.siguiente
                            aux2 = aux2.siguiente
                            repetidos += 1
                        elif aux1.columna < aux2.columna:
                            aux3.siguiente = Nodo(aux1.fila, aux1.columna, aux1.valor)
                            aux1 = aux1.siguiente
                        else:
                            aux3.siguiente = Nodo(aux2.fila, aux2.columna, aux2.valor)
                            aux2 = aux2.siguiente
                    elif aux1.fila < aux2.fila:
                        aux3.siguiente = Nodo(aux1.fila, aux1.columna, aux1.valor)
                        aux1 = aux1.siguiente
                    else:
                        aux3.siguiente = Nodo(aux2.fila, aux2.columna, aux2.valor)
                        aux2 = aux2.siguiente

        print(f"repetidos: {repetidos}")
    def mostrarFinal(self):
        aux = self.cabeza
        while aux is not None:
            print(aux.fila, aux.columna, aux.valor)
            aux = aux.siguiente


                            
                    




if __name__ == "__main__":

    filas = 3
    columnas = 3

    lista1 = Lista()
    lista2 = Lista()
    listaFinal = Lista()

    matriz1 = np.zeros((filas,columnas))
    matriz2 = np.zeros((filas,columnas))
    lista1.cargarMatriz(matriz1)
    lista1.cargarMatriz(matriz2)
    print("cargando lista enlazada 1")
    lista1.cargarListaEnlazada(matriz1,lista1,filas,columnas)
    print("\ncargando lista enlazada 2")
    lista2.cargarListaEnlazada(matriz2,lista2,filas,columnas)
    print("\nLISTA ENLAZADA 1\n")
    lista1.mostrarEnlazada(lista1.cabeza)
    print("\nlista enlazada 2\n")
    lista1.mostrarEnlazada(lista2.cabeza)
    print("LISTA ENLAZADA FINAL")
    listaFinal.ListaDefinitiva(lista1.cabeza,lista2.cabeza)
    listaFinal.mostrarFinal()


                
    

