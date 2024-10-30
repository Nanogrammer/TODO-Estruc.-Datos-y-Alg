import random
import numpy as np

class Trabajo:
    tiempoDemora: int
    tiempoRestante: int
    tiempoEspera: int
    tiempoLlegada : int
    atendido: bool

    def __init__(self) -> None:
        self.tiempoDemora = 0
        self.tiempoRestante = 0
        self.tiempoEspera = 0
        self.tiempoLlegada = 0

class ColaCircular:
    cola: np.array
    primer: int
    ultimo: int
    Tmaximo = 5
    cantidad: int
    tiempoActual: int



    def __init__(self) -> None:
        self.cola = np.full(50, None)
        self.primer = 0
        self.ultimo = 0
        self.cantidad = 0
        self.tiempoActual = 0
        #############
    


### informar cantidad de trabajos que quedaron sin atender
### Indicar el promedio de espera de los trabajos impresos

    def Simulacion(self):
        TClausura = 120
        impresora = 1
        z = 0
        cont  = 0

        while TClausura >= 0:
            
            trabajoX = Trabajo()

            if impresora == 1:
                trabajoX.tiempoLlegada = self.tiempoActual
                trabajoX.tiempoDemora = random.randint(1, 8)
                for trabajos in self.cola:
                    z += trabajos.tiempoDemora
                x = z

                # # for self.primer in range(len(self.cola)):
                # #     x = (self.cola[self.primer].tiempoDemora)
                # #     z += x

                trabajoX.tiempoEspera = int(x - trabajoX.tiempoDemora)
                trabajoX.tiempoRestante = int(self.Tmaximo - trabajoX.tiempoDemora)
                self.cola[self.ultimo] = trabajoX
                self.ultimo = (self.ultimo + 1) % self.cantidad
                trabajoX.atendido = False
                cont += 1
                self.cantidad += 1

            else:

                self.suprimir()
                calc = cont
                numeroNO = calc - 1
                ## elimina el primer elemento y el primero pasa a ser el segundo
                self.tiempoActual +=5
                impresora = 1
                TClausura -= self.tiempoActual

        

            print(f"La cantidad de elementos sin atender es {numeroNO}")
            promedio = x / cont
            print(f"el promedio de espera es: {promedio}")


    def suprimir(self):
        if self.cantidad > 0:
            self.cola[self.ultimo] = None
            self.ultimo = (self.ultimo - 1) % self.cantidad
        else:
            print("Cola vacia")




if __name__ == "__main__":
    cola = ColaCircular()
    cola.Simulacion()
