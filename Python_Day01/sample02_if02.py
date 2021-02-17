# 4의 배수를 확인

number = input('숫자 입력 : ')
number = int(number)

# 비교 방법1
if number%4 == 0:
    print('입력한 숫자는 4의 배수이다')
else:
    print('입력한 숫자는 4의 배수가 아니다')

# 비교 방법2
print('입력한 숫자는 4의 배수', end='')
if number%4 == 0 and number != 0:
    print('입니다')
else:
    print('가 아닙니다')