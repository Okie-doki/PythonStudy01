# class 작성
class AutoMobile:
    name = ''
    velocity = 0

    def velocityPlus(self):
        print('속도는 %d입니다' %self.velocity)
    def velocityDw(self):
        self.velocity -= 1
        if self.velocity < 0:
            self.velocity = 0
        print('속도는 {}입니다'.format(self.velocity))

# 객체 생성
ac = AutoMobile()
ac.velocityPlus()
ac.velocity = 20
ac.velocityDw()