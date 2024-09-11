def saluta(nome):
    print('Ciao', nome)

PI = 3.1415

class Cerchio:
    def __init__(self, raggio):
        self.raggio = raggio

    def calcolo_area(self):
        return self.raggio**2 * PI
