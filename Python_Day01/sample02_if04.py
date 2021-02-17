'''
입력 받은 점수로 성적 처리
90점 이상은 A
80점 이상은 B
70점 이상은 C
60점 이상은 D
나머지는 F
'''

number = int(input('점수 입력 : '))

if number >= 90:
    print('성적은 A입니다')
elif number >= 80:
    print('성적은 B입니다')
elif number >= 70:
    print('성적은 C입니다')
elif number >= 60:
    print('성적은 D입니다')
else:
    print('성적은 F입니다')