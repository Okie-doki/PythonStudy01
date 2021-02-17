# 2차원 배열
aList = [
    [0, 1, 2],
    [3, 4, 5],
    [7, 8, 9]
]

print('aList : ', aList)
print('aList[0] : ', aList[0])
print('aList[1] : ', aList[1])
print('aList[2] : ', aList[2])

# 값 4 출력
print('aList value 4 : ', aList[1][1])

# 값 8을 88로 수정
aList[2][1] = 88
print(aList)

aList.extend([[10, 20, 30]])
print(aList)
print(aList[3][0])
print(aList[3][1])