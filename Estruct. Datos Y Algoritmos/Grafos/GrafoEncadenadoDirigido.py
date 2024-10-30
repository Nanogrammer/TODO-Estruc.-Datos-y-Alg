from colasecuencial import Cola
import random

class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None

    def __str__(self):
        return f"{self.dato}"


class GrafoEncadenadoDirigido:
    def __init__(self):
        self.ArregloCabezas = [Nodo(random.randint(1, 100)) for _ in range(10)]

    def buscar_indice(self, valor):
        """Devuelve el índice del nodo con el valor especificado, o -1 si no se encuentra."""
        for i, nodo in enumerate(self.ArregloCabezas):
            if nodo.dato == valor:
                return i
        return -1  # Si no se encuentra

    def arista(self, nodoU, nodoV):
        """Crea una arista desde el nodo con valor nodoU al nodo con valor nodoV."""
        idxU = self.buscar_indice(nodoU)
        idxV = self.buscar_indice(nodoV)
        
        if idxU == -1 or idxV == -1:
            print(f"No se encontró uno de los nodos: {nodoU} o {nodoV}")
            return

        nuevo = Nodo(nodoV)
        if self.ArregloCabezas[idxU].siguiente is None:
            self.ArregloCabezas[idxU].siguiente = nuevo
        else:
            aux = self.ArregloCabezas[idxU].siguiente
            while aux.siguiente is not None:
                aux = aux.siguiente
            aux.siguiente = nuevo

    def adyacentes(self, idx):
        """Devuelve una lista de los valores adyacentes al nodo en el índice dado."""
        
        aux = []
        lista = self.ArregloCabezas[idx].siguiente
        while lista is not None:
            aux.append(lista.dato)
            lista = lista.siguiente
        return aux

    def MostrarCompArreglo(self):
        for i, nodo in enumerate(self.ArregloCabezas):
            print(f"Posición: {i} Valor: {nodo}")

    def bea(self, origen):
        """Búsqueda en amplitud (Breadth-First Search) desde un índice origen."""
        print(f"Nodo origen: {origen}")
        cola = Cola(len(self.ArregloCabezas))
        d = [999] * len(self.ArregloCabezas)
        d[origen] = 0
        cola.insertar(origen)

        while not cola.vacia():
            eliminado = cola.eliminar()
            x = self.adyacentes(eliminado)
            print(f"Adyacentes de {self.ArregloCabezas[eliminado].dato}: {x}")
            for adyacente_valor in x:
                adyacente_idx = self.buscar_indice(adyacente_valor)
                if adyacente_idx != -1 and d[adyacente_idx] == 999:
                    d[adyacente_idx] = d[eliminado] + 1
                    cola.insertar(adyacente_idx)
        return d


if __name__ == "__main__":
    Grafo = GrafoEncadenadoDirigido()

    # Crear aristas usando los valores de los nodos
    Grafo.arista(Grafo.ArregloCabezas[0].dato, Grafo.ArregloCabezas[3].dato)
    Grafo.arista(Grafo.ArregloCabezas[3].dato, Grafo.ArregloCabezas[0].dato)
    Grafo.arista(Grafo.ArregloCabezas[0].dato, Grafo.ArregloCabezas[1].dato)
    Grafo.arista(Grafo.ArregloCabezas[8].dato, Grafo.ArregloCabezas[9].dato)

    # Mostrar el grafo
    Grafo.MostrarCompArreglo()
    print("\nAdyacentes y distancias:")
    distancias = Grafo.bea(3)  # Iniciar búsqueda desde el índice 3
    print("Distancias:", distancias)
