class AutoMobile:
    name = ''
    velocity = 0

    def __init__(self, name, velocity):
        self.name = name
        self.velocity = velocity
    
    def velocityPlus(self):
        self.velocity += 1
        print('속도는 %d입니다' %self.velocity)
    def velocityDw(self):
        self.velocity -= 1
        if self.velocity < 0:
            self.velocity = 0
        print('속도는 {}입니다'.format(self.velocity))

car = AutoMobile('k5', 20)
print(car.name)
car.velocityPlus()
car.velocityDw()