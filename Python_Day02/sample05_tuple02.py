# 리스트는 중괄호[] 튜플은 소괄호()
aTuple = (1, 2, 3)

print(type(aTuple), aTuple)
print(aTuple[0])

#슬라이싱 1번자리 이후 모두 출력
print(aTuple[1:])

bTuple = (4, 5, 6)
print('aTuple id : ', id(aTuple))
aTuple = aTuple + bTuple
print('aTuple에 값 추가 : ', aTuple)
# +로 추가 시 새로운 변수로 생성(기존 변수 아님)
print('aTuple id : ', id(aTuple))

aTuple = (1, 2, 3)
aTuple = aTuple + bTuple[1:]
print(aTuple)