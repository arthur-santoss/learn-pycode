class Forma():
    def area(self):
        pass

class Quadrado(Forma):
    def __init__(self, lado):
        self.lado = lado

    def area(self):
        return self.lado ** 2
    
class Circulo(Forma):
    def __init__(self, raio):
        self.raio = raio

    def area(self):
        return 3.14 * (self.raio ** 2)

circulo = Circulo(3)
circulo_area = circulo.area()
print(f'Área do círculo: {circulo_area}')



quadrado = Quadrado(5)
quadrado_area = quadrado.area()
print(f'Área do quadrado: {quadrado_area}')