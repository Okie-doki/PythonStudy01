aTuple = 0, 1, 2 #튜플은 괄호 생략 가능
print(type(aTuple), aTuple)

# 튜플에는 모든 타입 복합으로 사용 가능
aTuple = 0, '할룽', '여보세요', 3.14
print(aTuple)
print(type(aTuple))
print(type(aTuple[0]))
print(type(aTuple[1]))
print(type(aTuple[2]))
print(type(aTuple[3]))

print(aTuple[2][3])
print(aTuple[2][-1])