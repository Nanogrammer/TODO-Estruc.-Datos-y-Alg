from cola import cola
import random
if __name__ == "__main__":
    contadorTrabajos = 0 #
    frecLlegada = 5 #
    tiempoImpresora =5 #
    tiempoTotal = 0
    tiempoMax = 60 #
    tiempoEspera = 0 #
    impresora = 1
    cola1 = cola()
    
    while tiempoTotal < tiempoMax and impresora!=0:
    
        tiempoLlegada = random.randint(0,1)
        if tiempoLlegada <= 1/frecLlegada:
            tiempoImpresionT = random.randint(1,10) 
            # print(tiempoImpresionT)
            cola1.insertar(tiempoImpresionT)
            
        
            tiempoTotal+=tiempoImpresionT
            if tiempoImpresora > tiempoImpresionT:
                impresora=1
                tiempoTotal+=tiempoImpresionT

            else:
                x = cola1.suprimir()
                y = x-tiempoImpresora
                cola1.insertar(y)
                tiempoTotal += tiempoImpresora

    print("______________________________________________________")
    print(f"TIEMPO TOTAL:{tiempoTotal}")
    print("______________________________________________________")
    

