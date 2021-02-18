class Car:
    name = ''
    velocity = 0

    def __init__(self, name, velocity):
        self.name = name
        self.velocity = velocity

# 상속받고자하는 클래스명을 클래스()에 넣음
class Sonata(Car):
    vender = ''

    def __init__(self):
        super().__init__('sonata', 30) # super는 부모 클래스를 지칭
        self.vender = 'Hundai'

aSonata = Sonata()
print(aSonata.name)
print(aSonata.velocity)
print(aSonata.vender)