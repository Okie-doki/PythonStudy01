# 동일한 파일(모듈)을 import 할 경우 진행 과정
# 동일한 모듈을 사용할 경우 처음 모듈만 1회 로드
print('1 start')
import sample08_imp01
print('2 start')
import sample08_imp01 as imp01
print('3 start')

sample08_imp01.tempFunction()
print(sample08_imp01.num)
print(sample08_imp01.string)
imp01.tempFunction()
print(imp01.num)
print(imp01.string)