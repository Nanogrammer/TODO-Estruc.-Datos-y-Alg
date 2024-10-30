from colasecConValor import Cola

class Nodo():
    dato: int
    siguiente: object

    def __init__(self,dato):
        self.dato = dato
        self.siguiente = None
    
    def __str__(self):
        return f"{self.dato}"



class GrafoEncadenadoDirigido:
    ArregloCabezas: list
    

    def __init__(self):
        
        self.ArregloCabezas = [Nodo(i) for i in range(10)]



    def arista(self,nodoU, NodoV):
        nuevo = Nodo(NodoV)
        print(f"Valor que entró {NodoV}")

        i = 0
        while i < len(self.ArregloCabezas) and self.ArregloCabezas[i-1].dato != nodoU:
            i+=1

        if self.ArregloCabezas[i-1].dato == nodoU:
            if self.ArregloCabezas[i-1].siguiente == None:
                self.ArregloCabezas[i-1].siguiente = nuevo
            else:
                aux = self.ArregloCabezas[i-1].siguiente
                while aux.siguiente is not None:
                    aux = aux.siguiente
                aux.siguiente = nuevo
                    
            
        
    def mostrar(self):
        for i in range(len(self.ArregloCabezas)):
            print(f"\nPosicion {i} del arreglo con valor: {self.ArregloCabezas[i]}")
            print(f"Adyacentes de {i}")
            y = self.adyacentes(i)
            print(f"Arreglo de adyacentes de {i}: {y}\n")

            
    def adyacentes(self, NodoU):
        
        aux = []
        lista = self.ArregloCabezas[NodoU].siguiente

        if lista == None:
            print("NO TIENE ADYACENTES")
            return aux
        
        while lista is not None:
            aux.append(lista.dato)
            lista = lista.siguiente
        
        print(f"Arreglo de adyacentes del nodo: {NodoU}: {aux}")

        return aux
    

    def MostrarArre(self):
        for i in range(len(self.ArregloCabezas)):
            print(f"Posicion: {i} Valor: {self.ArregloCabezas[i]}")
        

    def bea(self, origen):
        print(f"Nodo origen: {origen}")
        cola = Cola(len(self.ArregloCabezas))
        d = [999] * len(self.ArregloCabezas)
        d[origen] = 0

        cola.insertar(origen)
        while not cola.vacia():
            eliminado = cola.eliminar()
            x = self.adyacentes(eliminado)
            for i in x:
                if d[i] == 999:
                    d[i] = d[eliminado] +1
                    cola.insertar(i)
        return d


  
if __name__ == "__main__":
    Grafo = GrafoEncadenadoDirigido()
    
    Grafo.MostrarArre()
    Grafo.arista(0, 3)
    Grafo.arista(3,0)
    Grafo.arista(0,1)
    Grafo.arista(8,8)
    Grafo.arista(8,9)
    Grafo.arista(1,2)
    Grafo.arista(2,3)
    Grafo.arista(3,4)
    Grafo.arista(3,5)
    Grafo.arista(3,6)
    Grafo.arista(4,5)
    Grafo.arista(5,6)
    Grafo.arista(6,7)
    Grafo.arista(6,2)
    Grafo.arista(7,8)

    Grafo.mostrar()
    x= Grafo.bea(int(6))
    print(x)

