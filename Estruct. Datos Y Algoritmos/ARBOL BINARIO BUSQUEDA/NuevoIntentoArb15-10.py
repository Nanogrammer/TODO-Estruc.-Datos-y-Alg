import random

class Nodo:
    
    dato: int
    izquierda: object
    derecha: object

    def __init__(self,dato):
        self.dato = dato
        self.izquierda = None
        self.derecha = None
    def __str__(self):
        return f"{self.dato}"

class Arbol:
    raiz: Nodo
    niveles: int
    
    def __init__(self):
        self.raiz = None
        self.niveles = 0
    
    def insertarCabeza(self,valor):
        nuevo = Nodo(valor)
        if self.raiz == None:
            self.raiz = nuevo
            self.niveles +=1
        else:
            self.insertarRecursivo(self.raiz, nuevo)
    

    def insertarRecursivo(self, raiz, nuevo):
        if raiz == None:
            return
        if raiz.dato > nuevo.dato:
            if raiz.izquierda == None:
                raiz.izquierda = nuevo
            else:
                self.insertarRecursivo(raiz.izquierda, nuevo)
        elif raiz.dato < nuevo.dato:
            if raiz.derecha == None:
                raiz.derecha = nuevo
            else:
                self.insertarRecursivo(raiz.derecha, nuevo)
        else:
            return
    
    def inorden(self,raiz):

        if raiz == None:
            return 0
            
        self.inorden(raiz.izquierda)
        print(raiz.dato)
        self.inorden(raiz.derecha)
        
        

        
    def calculoNvl(self,raiz): ##  CALCULAR ALTURA DE ARBOL

        if raiz == None:
            return 0
            
        Nvl_izquierdas = self.calculoNvl(raiz.izquierda)
        Nvl_derechas = self.calculoNvl(raiz.derecha)
        
        if Nvl_izquierdas > Nvl_derechas:
            return Nvl_izquierdas +1
        else:
            return Nvl_derechas +1
        
    def calcularCantNodos(self,raiz):
        
        if raiz == None:
            return 0
        
        return 1 + self.calcularCantNodos(raiz.izquierda) + self.calcularCantNodos(raiz.derecha)
    
    def DevolverHermanoYpadre(self,raiz,NodoIngresado):
        
        if raiz == None:
            return
        
        if raiz.dato == NodoIngresado:
            print("EL NODO INGRESADO ES LA RAIZ INICIAL")
            return 
            
        if raiz.dato < NodoIngresado:
            if raiz.izquierda and raiz.izquierda.dato == NodoIngresado:
                print(f"El hermano derecho del Nodo ingresado es: {raiz.derecha}")
                print(f"El Padre del nodo ingresado es: {raiz}")
            elif raiz.derecha and raiz.derecha.dato == NodoIngresado:
                print(f"El hermano izquierdo del Nodo ingresado es: {raiz.izquierda}")
                print(f"El Padre del nodo ingresado es: {raiz}")
            else:
                self.DevolverHermanoYpadre(raiz.derecha, NodoIngresado)
        else:
            
            if raiz.izquierda and raiz.izquierda.dato == NodoIngresado:
                print(f"El hermano derecho del Nodo ingresado es: {raiz.derecha}")
                print(f"El Padre del nodo ingresado es: {raiz}")
            elif raiz.derecha and raiz.derecha.dato == NodoIngresado:
                print(f"El hermano izquierdo del Nodo ingresado es: {raiz.izquierda}")
                print(f"El Padre del nodo ingresado es: {raiz}")
            else:
                self.DevolverHermanoYpadre(raiz.izquierda, NodoIngresado)

    
    def DevolverHermanoYpadre2(self,raiz,NodoIngresado):
        
        ## en este metodo con la raiz actual verifica si sus hijos son iguales a el Valor de "NodoIngresado" y si no, 
        ## recorre el arbol si es menor el "NodoIngresado" al actual se va por la rama izquierda sino 
        ## por la rama derecha de forma recursiva recorriendo todo el arbol hasta encontrarlo
                                                                                                            
        if raiz == None:
            return
        
        if raiz.dato == NodoIngresado:
            print("EL NODO INGRESADO ES LA RAIZ INICIAL")
            return 
        
        if raiz.izquierda and raiz.izquierda.dato == NodoIngresado:
            hermano = raiz.izquierda
            print(f"El hermano izquierdo del nodo ingresado es: {hermano}")
            print(f"El Padre del nodo ingresado es: {raiz}")
            return raiz, hermano

        elif raiz.derecha and raiz.derecha.dato == NodoIngresado:
            hermano = raiz.derecha
            print(f"El hermano derecho del nodo ingresado es: {hermano}")
            print(f"El Padre del nodo ingresado es: {raiz}")
            return raiz, hermano

        if NodoIngresado < raiz.dato:
            self.DevolverHermanoYpadre(raiz.izquierda, NodoIngresado)
        else:
            self.DevolverHermanoYpadre(raiz.derecha, NodoIngresado)


###########################################################################        
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
                    print("    " * (nivel + 1) + "Der: None" )
                    
############################################################################










if __name__ == "__main__":
    op = 0
    
    Arbolito = Arbol()

    while op != "7":
        print("1. insertar")
        print("2. Mostrar")
        print("3. Imprimir graficamente")
        print("4. calcular altura")
        print("5. Calcular cantidad de nodos")
        print("6. Ver el padre y hermano de un nodo ingresado")

        op = input("ingrese una opcion\n")
        if op == "1":
            raizita = random.randint(7,1111)
            print(f"insertando valor: {raizita}")
            Arbolito.insertarCabeza(raizita)
        

        elif op == "2":
            Arbolito.inorden(Arbolito.raiz)
        
        elif op == "3":
            Arbolito.imprimir_arbol(Arbolito.raiz)
        
        elif op == "4":
            z = Arbolito.calculoNvl(Arbolito.raiz)
            print(f"-----------------El arbol tiene la Altura: {z}-------------------")
        elif op == "5":
            cantNodos = Arbolito.calcularCantNodos(Arbolito.raiz)
            print(f"-----------------Cantidad de nodos: {cantNodos}------------------")

        elif op == "6":

            valorIngresado = int(input("ingrese un valor a buscar\n"))
            print("resolucion 1") ## hecho por mi 
            Arbolito.DevolverHermanoYpadre(Arbolito.raiz,valorIngresado)
            print("resolucion 2") ## Optimizado
            Arbolito.DevolverHermanoYpadre2(Arbolito.raiz,valorIngresado)


            
            ### Pendiente ###
            ''' Ejercicio Nº 3: Codifique un programa que utilice el algoritmo de Huffman para comprimir
            un archivo de caracteres ya generado. Nota: hallar la frecuencia de cada caracter'''