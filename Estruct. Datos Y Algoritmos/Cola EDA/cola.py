class cola:
    cantidad : int
    maximo = 6
    cabeza : object


    def __init__(self) -> None:
        self.impresora = []
        self.cantidad = 0

    def insertar(self,n):
        self.impresora.append(n)
        self.cantidad+=1

    def suprimir(self):
        if self.vacio()!=0:
            self.cantidad-=1
            print(self.impresora[self.cantidad])
            return self.impresora.pop(0)
        else:
            return None
    
    def vacio(self):
        if self.cantidad==0:
            print("cola vacia\n")
            res = 0
        else:
            res = 1
        return res