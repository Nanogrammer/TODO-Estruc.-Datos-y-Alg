class Arreglo():
    letra: str
    contador: int

    def __init__(self,letra) -> None:
        self.letra = letra
        self.contador = 0
    
    def __str__(self) -> str:
        if self.contador > 1:
            return f"--La letra: '{self.letra}' Se repite: '{self.contador}' veces."
        else:
            return f"--La letra: '{self.letra}' Se repite: '{self.contador}' sola vez."

class Nodo:

    letra: str
    contador: int
    siguiente: object
    izquierda: object
    derecha: object
    anterior: object

    def __init__(self,letra,contador):
        self.letra = letra
        self.contador = contador
        self.derecha = None
        self.izquierda = None
        self.siguiente = None
        self.anterior = None
    
    
class Arbol:
    raiz: Nodo
    cabeza: object
    guardar: list
    caracteres: int

    def __init__(self,raiz=None):

        self.raiz = raiz
        self.cabeza = None
        self.guardar = []
        
    
    def crear(self,dato):
        nuevo = Arreglo(dato)
        
        i = 0
        
        if len(self.guardar) == 0:
            nuevo.contador +=1
            self.guardar.append(nuevo)
        
        else:     
            
            while i < len(self.guardar) and nuevo.letra != self.guardar[i].letra:
                i += 1
            if i < len(self.guardar) and nuevo.letra == self.guardar[i].letra:
                self.guardar[i].contador += 1
            else:
                nuevo.contador += 1
                self.guardar.append(nuevo)

            
    def mostrar(self):
        for i in self.guardar:
            print(i)
        
    def enlazar(self):

        for i in range(len(self.guardar)):
            nuevo = Nodo(self.guardar[i].letra, self.guardar[i].contador)
            if self.cabeza == None:
                self.cabeza = nuevo
            else:
                aux = self.cabeza
                while aux.siguiente != None:
                    aux = aux.siguiente
                    
                aux.siguiente = nuevo
                aux.siguiente.anterior = aux
                
    
                
    def mostrarEnlaz(self):
        aux = self.cabeza 
        while aux != None:
            print(f"La letra: '{aux.letra}', Se repitió : '{aux.contador}' veces")
            aux = aux.siguiente


    def suprimirFusion(self):
        aux = self.cabeza

        while aux.siguiente != None:
            
            aux1 = aux.siguiente
            letra = str(aux.letra + aux1.letra)
            contador = int(aux.contador + aux1.contador)
            reemplazo = Nodo(letra, contador)
            reemplazo.izquierda = aux
            reemplazo.derecha = aux1

            while aux1.siguiente != None and reemplazo.contador > aux1.siguiente.contador:
                aux1 = aux1.siguiente
            
            aux3 = aux1.anterior
            if aux3 is not None:
                aux3.siguiente = reemplazo
                reemplazo.siguiente = aux1.siguiente
                reemplazo.anterior = aux3
                if aux1 is not None:
                    aux1.anterior = reemplazo
            aux = aux.siguiente




if __name__ == "__main__":
    arbolito = Arbol()
    frase = "Unas ganas de papiar tengo, o tomar un mate"
    print(f"La frase es: {frase}\n")
    arbolito.caracteres = list(frase)
    for i in range(len(arbolito.caracteres)):
        arbolito.crear(arbolito.caracteres[i])
    arbolito.guardar.sort(key=lambda x: x.contador, reverse=True)
    # arbolito.mostrar()
    z = int(0)
    arbolito.enlazar()

    arbolito.mostrarEnlaz()
    arbolito.suprimirFusion()
    print("--------------------------------MUESTRA DESPUES DE LA FUSION-------------------------------")
    arbolito.mostrarEnlaz()    

        


    