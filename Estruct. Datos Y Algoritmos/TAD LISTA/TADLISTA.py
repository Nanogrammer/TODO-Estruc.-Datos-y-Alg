
import numpy as np
class Lista:
    contador: int
    cabeza: object
    anterior: object
    lista = np.full(10,None)

    def __init__(self) -> None:
        self.contador = 0
        self.anterior = None
        self.cabeza= None
        self.maximo = 6



    def insertar(self):
        
        dato = input("ingrese un nombre\n")
        if self.lleno() is not True:
            nuevo = Nodo(dato)
            self.contador+=1

            if self.cabeza == None: ## carga cabeza
                self.cabeza = nuevo
                self.cabeza.setanterior(None)
                self.cabeza.setsiguiente(None)
                self.lista[self.contador-1] = nuevo.dato
        
                
            else:

                aux = self.cabeza
                while aux.getsiguiente() != None and nuevo.dato > aux.getdato():
                    
                    aux.setanterior(aux)
                    aux = aux.getsiguiente()

                

                if self.cabeza.getdato() > nuevo.dato: ## en el principio

                    nuevo.setsiguiente(self.cabeza)
                    self.cabeza.setanterior(nuevo)
                    self.cabeza = nuevo
                    self.lista[self.contador-1] = nuevo.dato
                    print(f"1.INSERCION EN EL PRINCIPIO {aux.getdato()}--\n")



                    
                elif aux.getdato() >= nuevo.dato: ##  insercion en el medio??
                    nuevo.setanterior(aux.getanterior())
                    nuevo.setsiguiente(aux)
                    aux.getanterior().setsiguiente(nuevo)
                    aux.setanterior(nuevo)
                    self.lista[self.contador-1] = nuevo.dato

                if aux.getsiguiente() == None: ## llegó al final de la lista enlazada pero no del arreglo 

                    if nuevo.dato >= aux.getdato(): ## al final
                        aux.setsiguiente(nuevo)
                        nuevo.setanterior(aux)
                        nuevo.setsiguiente(None)
                        self.lista[self.contador-1] = nuevo.dato
                        
                elif aux.getsiguiente()!=None:

                    nuevo.setanterior(aux.getanterior())   ## insercion en medio
                    nuevo.setsiguiente(aux)  
                    aux.getanterior().setsiguiente(nuevo)
                    aux.setanterior(nuevo)
                    self.lista[self.contador-1] = nuevo.dato
                    
        else:
            print("\n ------------------El arreglo está LLENO no se puede insertar------------\n")            

    def mostrar(self):
        print("\n ELEMENTOS EN EL ARREGLO")
        for x in self.lista:
            print(x)

    def suprimirLE(self):
        if self.vacio() == False:
            aux = self.cabeza
            while aux != None and aux.getdato() != self.lista[self.contador-1]: ## busca que el dato del arreglo y de la lista sean iguales y suprime
                aux = aux.getsiguiente()
            if aux.getdato() == self.lista[self.contador-1]:
                print(f"SUPRIMIENDO: {self.lista[self.contador-1]}")
                self.lista[self.contador-1] = None
                aux.setanterior(None)
                aux.setdato(None)
                self.contador-=1
        

    def vacio(self):
        if self.contador != 0:
            result = False
            
        else:
            print("----------------EL ARREGLO ESTA VACIO NO SE PUEDE SUPRIMIR--------------------\n")
            result = True
    

        return result

    def lleno(self):
        if self.contador == self.maximo:
            result = True
        else:

            result = False
        return result

    def mostrar2(self):
        aux = self.cabeza
        print("\n ELEMENTOS EN LA LISTA ENLAZADA")
        while aux!=None:
            print(f"-------------{aux.getdato()}------------") 
            aux = aux.getsiguiente()




class Nodo:

    dato: object
    siguiente: object
    anterior: object



    def __init__(self,dato):
        self.dato = dato
        self.siguiente = None
        self.anterior = None

    def __str__(self) -> str:
        return f"dato: {self.dato}"
    
    
    def getdato(self):
        return self.dato
    def getsiguiente(self):
        return self.siguiente
    def setsiguiente(self,v):
        self.siguiente = v
    def setanterior(self,v):
        self.anterior = v
    def getanterior(self):
        return self.anterior
    def setdato(self,v):
        self.dato = v




if __name__ == "__main__":

    op = 0
    L = Lista()

    while op !="7":
        print("1. Insertar")
        print("2. Mostrar EL ARREGLO NUMPY")
        print("3. Mostrar LA LISTA ENLAZADA")
        
        print("5. suprimir con enlazada")
        print("7. Salir")
        op = input("inserte una opcion\n")
        
        if op == "1":
            L.insertar()
        elif op == "2":

            L.mostrar()
        elif op == "3":
            L.mostrar2()
    
        
        elif op =="5":
            L.suprimirLE()

        elif op == "7":
            print("SALIENDO\n")
            break

        else:
            op = input("inserte una opcion\n")

        
