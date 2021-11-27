class Titik:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Segitiga:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
    @property
    def luas(self):
        x1, y1 = self.a.x, self.a.y
        x2, y2 = self.b.x, self.b.y
        x3, y3 = self.c.x, self.c.y
        return 0.5*abs((x2 - x1)*(y3 - y1) - (x3 - x1)*(y2 - y1))

# input
A, B = Titik( 2, 14), Titik(8, 11)
C, D = Titik(14, 10), Titik(6,  6)
E, F = Titik( 9,  4), Titik(1,  1)
poligon = [
    Segitiga(A, B, D),
    Segitiga(B, D, E),
    Segitiga(B, C, E),
    Segitiga(D, E, F),
]

# proses
luas = 0
for segitiga in poligon:
    luas += segitiga.luas

# output
print(luas)