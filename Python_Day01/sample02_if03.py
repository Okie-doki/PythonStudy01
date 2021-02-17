number = input('속도 입력 : ')
number = int(number)

# if elif else
if 80 < number:
    print('고속 주행입니다')
elif 60 < number:
    print('일반 주행입니다')
else:
    print('저속 주행입니다')