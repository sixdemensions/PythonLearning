#在Python程序中，用if语句实现条件判断
age = 20
if age >=18:
    print('your age is',age)
    print('adult')
##else注意不要少写了冒号:
else:
    print('your age is',age)
    print('minor')
#elif是else if的缩写，完全可以有多个elif，所以if语句的完整形式就是：
#if <条件判断1>:
#    <执行1>
#elif <条件判断2>:
#    <执行2>
#elif <条件判断3>:
#    <执行3>
#else:
#    <执行4>
#if语句执行有个特点，它是从上往下判断，如果在某个判断上是True，把该判断对应的语句执行后，就忽略掉剩下的elif和else，所以，请测试并解释为什么下面的程序打印的是minor：
age = 16
if age >=18:
    print('adult')
elif age>=10:
    print('teenager')
else:
    print('kid')
#int()函数配合输入
birth = int(input('Birth year:'))
if birth<2000:
    print('00前')
else:
    print('00后')
