import numpy as np
class ColaCircular:
    Colita: np.array
    tope: int
    cabeza : int
    def __init__(self) -> None:
        self.Colita = np.full(5,None)
        self.tope= 1
        self.cabeza = 0
    
    def insertar(self,elem):

            if self.lleno() == False:
                self.Colita[self.tope] = elem
                print(self.Colita[self.tope])
                self.tope += 1
            
            elif self.vacio() == True and self.cabeza == self.tope:
                self.tope = 0
                if (self.tope + 1) == None:
                    self.Colita[self.tope+1] = elem
                    print(self.Colita[self.tope])
                    self.tope +=1
                    
                else:
                     print("No se puede cargar están llenas todas las posiciones")


    def suprimir(self):

        if self.vacio() == False:
                print(self.Colita[self.cabeza])
                x = self.Colita[self.cabeza] 
                self.Colita[self.cabeza] = None
                self.cabeza += 1
                print(x)

        elif self.vacio() == False and self.cabeza == 4:
                self.cabeza = 0
                if self.Colita[self.cabeza] != None:
                     x = self.Colita[self.cabeza]
                     self.Colita[self.cabeza] = None
                     self.cabeza +=1
                     print(x)

        return x
    

    def lleno (self):
        if self.tope < 5:
            result = False
        else:
            result = True
        return result
    
    def vacio(self):
        if self.tope > 0:
            result = False
        else:
            result = True
        return result
        
if __name__ == "__main__":
     Cola1 = ColaCircular()
     Cola1.insertar(1)
     Cola1.insertar(2)
     Cola1.insertar(3)
     Cola1.insertar(4)
     Cola1.insertar(5)
     Cola1.insertar(6)
     Cola1.suprimir()
     Cola1.insertar(7)
     
