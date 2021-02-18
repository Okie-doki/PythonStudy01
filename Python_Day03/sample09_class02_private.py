class AutoMobile:
    # __name = '' <- private 설정
    __name = ''
    __velocity = 0

    #__init__ 초기화, 1회만 실행
    def __init__(self, name):
        self.__name = name #private 설정 시 동일한 모든 변수에 __ 작성

    #private 작성 시 getter / setter 로 캡슐화
    def getName(self):
        return self.__name
    def getVelocity(self):
        return self.__velocity
    def setName(self, name):
        self.__name = name
    def setVelocity(self, velocity):
        self.__velocity = velocity

    def velocityPluse(self):
        self.__velocity += 1
        print('속도는 %d입니다' %self.__velocity)
    def velocityDw(self):
        self.__velocity -= 1
        if self.__velocity < 0:
            self.__velocity = 0
        print('속도는 {}입니다'.format(self.__velocity))

aAutoMobile = AutoMobile('my car')
aAutoMobile.velocityPluse()
print('car name : ', aAutoMobile.getName())
print('car speed : ', aAutoMobile.getVelocity())