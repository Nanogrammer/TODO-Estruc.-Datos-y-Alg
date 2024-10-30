class Nodo:
    anterior: None
    siguiente:None
    izquierda: None
    derecha: None
    valor: int

    def __init__(self,valor) -> None:
        self.anterior = None
        self.siguiente = None
        self.derecha = None
        self.izquierda = None
        self.valor = valor

class Arbol():
    raiz: object
    cabeza : object

    def __init__(self) -> None:
        self.raiz = None
        self.cabeza = None


    def cabeziña(self,valor):
         nuevo = Nodo(valor)
         self.cabeza = nuevo
         return self.cabeza
        

    def insertar(self, raiz):
            nuevo = Nodo(valor)
            if raiz == None:
                raiz = nuevo
                print(f"Cargando raiz: {raiz.valor}")
            else:
                aux = raiz
                if nuevo.valor < aux.valor:
                    if aux.izquierda == None:
                        aux.izquierda = nuevo
                        print(f"Cargando izquierda: {aux.izquierda.valor}")
                    else:
                        aux = aux.izquierda
                        self.insertar(aux, nuevo.valor)

                elif nuevo.valor > aux.valor:
                    
                    if aux.derecha == None:
                        aux.derecha = nuevo
                        print(f"Cargando derecha: {aux.derecha.valor}")
                    else:
                        aux = aux.derecha
                        self.insertar(aux,nuevo.valor)

                print("insertado con exitación")
        
    def mostrar(self):
        aux = self.cabeza
        while aux != None:
            # print(f"Izquierda:{aux.valor}")
            print(f"Derecha:{aux.izquierda.valor}")
            # aux = aux.izquierda
            aux = aux.derecha
        aux2 = self.cabeza
        while aux2 != None:
            print(f"izquierda :{aux2.derecha.valor}")
            aux2 = aux2.izquierda
            


if __name__ == "__main__":
    arbolito = Arbol()
    op = 0

    raiz = None

    while op != "7":

        print("1. insertar")
        print("2. mostrar")
        op = input ("ingrese opcion\n")
        

        if op == "1":
            x = int(input("ingrese un valor\n"))
            arbolito.insertar(raiz,x)
        elif op == "2":
            arbolito.mostrar()
        else:
            op = input ("ingrese opcion\n")
            