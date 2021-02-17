# 함수 return 값으로 여러값을 받을 수 있음
# 튜플로 return
def spring(num1, num2):
    return num1 + 100, num2 + 2000

temp = spring(100, 200)
print(type(temp), temp)

# return 값의 개수만큼 변수를 준비해서 받을 수 있음
result1, result2 = spring(111, 222)
print(type(result1), result1)
print(type(result2), result2)