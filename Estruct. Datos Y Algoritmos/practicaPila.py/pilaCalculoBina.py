import numpy as np

class Pila:
    tope: int
    items: np.array
    

    def __init__(self) -> None:
        self.tope = 0
        self.items = np.full(5, None)


    def CalculoBinario(self,X):
        resultado = X
        self.tope = 0
        resto = 0

        if self.tope < 8:    ### Pregunta si no está lleno
            while resultado > 0:
                resto = resultado % 2
                print(f"Resultado: {resultado}")
                print(f"Cargado: {resto}")  ## PARA MOSTRAR
                self.items[self.tope] = resto
                self.tope += 1
                resultado = resultado // 2

        print("---------------DESAPILANDO---------------")
        while self.tope < 8:
            self.suprimir()
            

    def suprimir(self):
        if self.tope > 0: ## pregunta si no está vacio
            self.tope -= 1
            valor = self.items[self.tope]
            self.items[self.tope] = None
            print(f"Desapilado: {valor}") ## para mostrar
        
if __name__ == "__main__":
    pilita = Pila()
    pilita.CalculoBinario(25)
    


