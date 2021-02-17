aList = [23, 65, 34, 3, 35, 5, 55]
print('aList : ', aList)

# sort 오름차순 정렬
aList.sort()
print('aList sort : ', aList)

# reverse 역순(정렬 아님)
aList.reverse()
print('aList reverse : ', aList)

# insert(몇 번쨰, 값)
aList.insert(2, 77)
print('aList insert(2, 77) : ', aList)

# pop() 마지막 번째 값 출력과 해당 값 제거
temp = aList.pop()
print('aList pop : ', aList)
print('temp : ', temp)

# pop(3) 4번째 순서의 값 출력 및 제거
temp1 = aList.pop(3)
print('aList pop(3) : ', aList)
print('temp1 : ', temp1)

# extend() 리스트 추가
aList.extend([1, 99, 200, 300])
print('aList extend : ', aList)

bList = [1, 2, 3]
cList = [4, 5, 6]
# 리스트값 합치기
dList = bList + cList
print('bList + cList : ', dList)

# 리스트값 모두 제거
dList.clear()
print('dList clear : ', dList)

# del 원하는 위치의 리스트값 제거
del aList[1]
print('aList del : ', aList)

aList.append(34)
print('aList append : ', aList)
# count를 이용하여 해당 리스트에 값이 몇개 있는지 확인
print('aList 34 count : ', aList.count(34))