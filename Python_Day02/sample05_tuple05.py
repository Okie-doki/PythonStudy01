aTuple = tuple(range(1, 10)) #range 활용, tuple 강제 형변환

print(type(aTuple), aTuple)

aTuple1 = tuple(range(0, 100, 13))
print(aTuple1)

aList = list(range(0, 100, 13)) #list 강제형변환
print(type(aList), aList)

a = '가나다라'
a = a * 3
print(a)

bTuple = tuple(range(10))
print(bTuple)
# in을 이용하여 튜플에 값10이 있는지 확인
# 존재할 경우 true 없을 경우 false
print(10 in bTuple)

tmp = 3
if tmp in bTuple:
    print('찾았다')

aRange = range(2, 20, 5)
print(type(aRange), aRange)
print(aRange[0])
print(aRange[3])

aTuple = tuple(aRange)
print(aTuple)