import random

class Nodo:
    dato : int
    izquierda: object
    derecha: object

    def __init__(self,dato) -> None:
        self.izquierda = None
        self.derecha = None
        self.dato = dato
    
    def __str__(self) -> str:
        return f"{self.dato}"

class Arbol:
    raiz: Nodo

    def __init__(self) -> None:
        self.raiz = None


    def insertar(self,valor):
        
        nuevo = Nodo(valor)
        if self.raiz == None:
            self.raiz = nuevo
            print(f"Cabeza:{nuevo}")
        else:
            self.insertar_Recurs(self.raiz, nuevo)

        
    def insertar_Recurs(self, actual ,nuevo):
        
        if actual is None:
            return

        if nuevo.dato < actual.dato:
            if actual.izquierda == None:    
                actual.izquierda = nuevo
            else:
                self.insertar_Recurs(actual.izquierda, nuevo)
        elif nuevo.dato > actual.dato:
            if actual.derecha == None:    
                actual.derecha = nuevo
            else:
                self.insertar_Recurs(actual.derecha, nuevo)
        else:
            return

    def inorder(self,raiz):
        
        if raiz != None:
            
            self.inorder(raiz.izquierda)
            print(raiz.dato)
            self.inorder(raiz.derecha)
            
    def imprimir_arbol(self, nodo, nivel=0, prefijo="Raiz: "):
        """Método para mostrar el árbol de manera gráfica"""
        if nodo is not None:
            print("    " * nivel + prefijo + str(nodo.dato))
            if nodo.izquierda is not None or nodo.derecha is not None:
                if nodo.izquierda:
                    self.imprimir_arbol(nodo.izquierda, nivel + 1, "Izq: ")
                else:
                    print("    " * (nivel + 1) + "Izq: None")
                if nodo.derecha:
                    self.imprimir_arbol(nodo.derecha, nivel + 1, "Der: ")
                else:
                    print("    " * (nivel + 1) + "Der: None")
    

if __name__ == "__main__":
    Arbolito = Arbol()
    op = 0
    while op != "5":
        op = input("ingrese una opcion\n")
        if op == "1":
            valor = random.randint(1,100)
            Arbolito.insertar(valor)
            print(f"insertado: {valor}")
        elif op == "2":
            print("MUESTRA DEL ARBOL")
            Arbolito.inorder(Arbolito.raiz)
        elif op == "3":
            Arbolito.imprimir_arbol(Arbolito.raiz)
        else:
            op = input("ingrese una opcion\n")            
