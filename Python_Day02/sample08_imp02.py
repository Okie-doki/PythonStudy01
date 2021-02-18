import sample08_imp01

print('===import sample08_imp01===')
sample08_imp01.tempFunction()
print(sample08_imp01.num)
print(sample08_imp01.string)

# as '별명'으로 별명 대체 가능
print('===import sample08_imp01 as imp01===')
import sample08_imp01 as imp01
imp01.tempFunction()
print(imp01.num)
print(imp01.string)
