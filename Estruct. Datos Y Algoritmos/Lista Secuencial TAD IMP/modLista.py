import numpy as np
class Lista:
    L = np.full(6,None)
    tope = -1
    maximo = 6

    def insertar(self,n):
        if self.lleno()==1:
            
            self.L[self.tope+1] = n
            self.tope+=1
        

    def insertarEnMedio(self,indice,n):
        if self.lleno()==1:
            indice = int(indice)
            if self.L[indice-1] != None:
                self.L[self.tope+1] = self.L[self.tope]
                aux = self.tope
                
                while aux != indice-1 :
                    self.L[aux] = self.L[aux-1]
                    aux -=1
                    
                self.L[indice-1] = n
                self.tope+=1
                
            else:
                self.L[indice-1] = n
                self.tope+=1

    def mostrar(self):
        for x in self.L:
            print(x,"\n")



    def lleno(self):
        if self.tope >= self.maximo:
            print("lista llena raviol")
        else:
            return int(1)

    def vacio(self):
        if self.tope == -1:
            print("la lista esta vacia capo")
        else: 
            return int(1)
        
    def suprimir(self):
        if self.vacio()==1:
            self.L[self.tope] = None
            self.tope-=1


    