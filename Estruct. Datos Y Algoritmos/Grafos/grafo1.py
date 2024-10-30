import networkx as nx
import numpy as np

class GrafoSec:
    matriz: np.array

    def __init__(self):
        self.matriz = np.zeros((5, 5))

if __name__ == "__main__":
    Grafo = nx.Graph()
    Matriz = GrafoSec()
    

    # Añadir nodos y aristas
    Grafo.add_edges_from([(1, 2), (1, 3), (2, 4), (3, 4), (4, 5)])

    print("Nodos:", Grafo.nodes())
    print("Aristas:", Grafo.edges())

    # Crear la matriz de adyacencia
    for i in Grafo.nodes():
        for j in Grafo.nodes():
            if (i, j) in Grafo.edges() or (j, i) in Grafo.edges():
                Matriz.matriz[i-1][j-1] = 1  # Restar 1 para indexar correctamente

    print(Matriz.matriz)


    