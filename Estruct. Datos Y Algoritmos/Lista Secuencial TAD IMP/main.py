from modLista import Lista

if __name__== "__main__":
    L = Lista()
    op = 0
    while op !="5":
        print("1. Insertar al final?")
        print("2. Insertar en una posicion especifica?")
        print("3. mostrar Lista?")
        print("4. suprimir")
        print("5. salir\n")

        
        op = input("ingrese una opcion")
        
        if op == "1":
            n = input("ingrese un Valor a insertar\n")
            L.insertar(n)
        elif op == "2":
            x = input("inserte el valor")
            indice = input("inserte un indice ocupado de preferencia")    
            L.insertarEnMedio(indice,x)
            
        elif op == "3":
            L.mostrar()
        elif op == "4":
            L.suprimir()
        elif op  == "5":
            print("saliendo")

        else:
            op = 0
