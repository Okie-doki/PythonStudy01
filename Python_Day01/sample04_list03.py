# 리스트 선언 후 append로 값 삽입
array = []
array.append(100)
array.append(200)
array.append(300)
array.append(400)

for i in array:
    print(i)

# remove 명령어로 원하는 값 삭제
array.remove(200)

for i in array:
    print(i)