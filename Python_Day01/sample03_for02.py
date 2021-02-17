#for문을 이용하여 1에서 10까지 합 구하기
sum = 0
for i in range(1, 11, 1):
    sum += 1
print('sum : %d' %sum) #%d 10진수 출력

#for문을 이용하여 1에서 10까지의 식과 합 출력
sum = 0
for i in range(1, 11, 1):
    if i < 10:
        print('%d + ' %i, end='')
    elif i == 10:
        print('%d = ' %i, end='')
    sum += i
print('%d' %sum)