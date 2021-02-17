def mydef01():
    i, j = 10, 20
    print(i+j)
mydef01()

def mydef02(i, j):
    print(i+j)
mydef02(10, 20)

#계산할 숫자 2개와 사칙연산 입력
def mydef03(i, j, k):
    if k == '+':
        print(i+j)
    elif k == '-':
        print(i-j)
    elif k == '*':
        print(i*j)
    elif k == '/':
        print(i/j)
n = int(input("첫 번째 숫자 입력 :"))
m = int(input("두 번째 숫자 입력 :"))
p = input("연산자를 입력(+, -, *, /) : ")
mydef03(n, m, p)
