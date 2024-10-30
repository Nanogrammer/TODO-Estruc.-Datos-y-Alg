import numpy as np
if __name__ == "__main__":

    def factorial(n):
        pila = []
        resultado = 1
        while n>0:
            pila.append(n)
            n-=1
        while pila:
            actual = pila.pop() 
            resultado = resultado * actual
        return resultado
    
        




    x = factorial(3)
    print(x)


    

    