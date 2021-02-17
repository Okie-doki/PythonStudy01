aDict = {
    '이름' : '홍길동',
    '나이' : 50,
    10 : '10만원'
}

print(aDict)
print(aDict.keys()) #key값 모두 출력
print(aDict.values()) #value값 모두 출력
del aDict['나이'] #del을 이용하여 원하는 key값 삭제
print(aDict)
print('이름' in aDict)
print('나이' in aDict)