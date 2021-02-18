class Car:
    name = ''
    velocity = 0

    def __init__(self, name, velocity):
        self.name = name
        self.velocity = velocity

class Car2:
    color = ''

    def __init__(self, color):
        self.color = color

# 다중 상속
class Sonata(Car, Car2):
    vender = ''

    def __init__(self):
        Car.__init__(self, 'sonata', 30)
        Car2.__init__(self, 'blue')
        self.vender = 'Hundai'

aSonata = Sonata()
print(aSonata.vender)
print(aSonata.name)
print(aSonata.velocity)
print(aSonata.color)