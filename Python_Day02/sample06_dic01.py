# 딕셔너리 자료형은 key : value 를 가지며,
# key값은 중복 사용 불가
aDict = {
    '이름' : '홍길동',
    '나이' : 50,
    10 : '10만원'
}

print(type(aDict), aDict)
print(aDict['이름'])
print(aDict['나이'])
print(aDict[10])