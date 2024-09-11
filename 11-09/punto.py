from math import sqrt

class Punto:
    def __init__(self, ascissa, ordinata):
        self.x = ascissa
        self.y = ordinata

    # def stampa_punto(self):
    #     print( "(" self.x ",", self.y, ")")

    def muovi_punto(self, dx, dy):
        self.x += dx
        self.y += dy

    def distanza_origine(self):
        return sqrt(self.x**2 + self.y**2)

Punto1 = Punto(2,3)
print("La distanza dall'origine è", Punto1.distanza_origine())
Punto1.muovi_punto(-2, -3)
print(Punto1.distanza_origine())