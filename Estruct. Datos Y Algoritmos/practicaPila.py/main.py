from clase_pila import Pila, factorial


def Menu():
    op = 0
    print("1. Insertar numero")
    print("2. mostrar pila")
    print("3. suprimir")
    print("4. calcular factorial")
    print("5. SALIR")
    op = input("ingrese una opcion")
    return op
#----------------------------------------------------------------------------------------------------

if __name__=="__main__":
    pilita = Pila()
    op = 0
    while op != "5":    
        op = Menu()

        if op == "1": 
            n = input("ingrese un numero entero\n")
            pilita.insertar(int(n))

        elif op == "2":
            pilita.mostrarPila()
        elif op == "3":    
            pilita.suprimir()

        elif op == "4":
            x=input("ingrese un entero menor a 10")
            factorial(int(x))
        elif op == "5":
            break
        else:
            op = Menu()
        

