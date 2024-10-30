import random
class cola:
    cola: list


    def RepreCola(self):
        cajero = 0
        frecLleg = 3
        tpoCajero = 4
        Tsimul = 60
        contador = 0
        acumulador = 0
        reloj = 0
        tEspera = 0

        r = random.randint(0,1)
        if Tsimul > r:
            if r <= 1/frecLleg:
                self.cola.append(r)
            if cajero == 0:
                if self.vacio() is false:
                    self.suprimir(self.cola,x)
                    tEspera = r - x
                    acumulador = acumulador + tEspera
                    contador += 1
                    cajero = tpoCajero
                else:
                    cajero -= 1

            reloj += 1
        promedio = acumulador / contador




