class Nodo:
    izquierda: object
    derecha: object
    dato: int
    contDato: int

    def __init__(self,dato) -> None:
        self.derecha = None
        self.izquierda = None
        self.dato = int(dato)
        self.contDato = 0
    



class Arbol:
    raiz: object
    cabeza: object
    
    def __init__(self) -> None:
        self.raiz = None
        self.cabeza = None

    def cargaRaiz(self, dato, raiz=None):
        
        if raiz == None:
            raiz = self.cabeza
        
        nuevo = Nodo(int(dato))

        if self.cabeza == None:
            self.cabeza = nuevo
            raiz = self.cabeza
            print("carga de la cabeza")
        
        else:
            aux = raiz

            if aux.dato < self.cabeza.dato:
                cambio = int(self.cabeza.dato)
                self.cabeza = int(raiz.dato)
                raiz = cambio
        
            elif nuevo.dato > aux.dato:
                if aux.derecha == None:
                    aux.derecha = nuevo
                    print("carga por la derecha")
                else:
                    self.cargaRaiz(aux.derecha)

            elif nuevo.dato < aux.dato:
                if aux.izquierda == None:
                    aux.izquierda = nuevo
                    print("carga por la izquierda")
                
                else:
                    self.cargaRaiz(aux.izquierda)

    def inorden(self,raiz,i):     
        
        if raiz != None:
            i+=1
            self.inorden(raiz.izquierda,i)
            
            print(f"{i}:{raiz.dato}")
            i+=1
            self.inorden(raiz.derecha,i)


if __name__ == "__main__":
    arbol1 = Arbol()
    x = 0
    i = 0
    raiz = None
    while x != "7":
        print("1. cargar")
        print("2. mostrar")
        x = input("ingrese una opcion\n")
        
        if x == "1":
            dato = int(input("ingrese un valor para guardar \n"))
            arbol1.cargaRaiz(dato,raiz)
        elif x == "2":
            arbol1.inorden(arbol1.cabeza,i)
        else:
            x = input("ingrese una opcion\n")

