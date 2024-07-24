#练习BMI计算(变量类型中含有’字符串‘后面需要添加：用于标记输入变量)
print('Please input your height and weight(with "and" calculate )')
height = float(input('Input your height (centimeters):'))
weight = float(input('Input your weight (kilograms):'))
bmi = weight/((height/100)**2)
print(bmi)
if bmi>= 32:
    print('Extreme Obesity')
elif bmi>=28 and bmi< 32:
    print('Obese')
elif bmi>=25 and bmi<28:
    print('over weight')
elif bmi >=18.5 and bmi<25:
    print('healthy')
else:
    print('under weight')
#and运算实际不需要，因为从大到小进行判断，不会跳过条件。
print('Please input your height and weight(without "and" cuaculate)')
height = float(input('Input your height (centimeters):'))
weight = float(input('Input your weight (kilograms):'))
bmi = weight/((height/100)**2)
print(bmi)
if bmi>= 32:
    print('Extreme Obesity')
elif bmi>=28:
    print('Obese')
elif bmi>=25:
    print('over weight')
elif bmi >=18.5:
    print('healthy')
else:
    print('under weight')
#如果两个条件是从最小，而又使用大于进行判断，就可能出现终止条件，或者反之，从最大开始，而又用小于进行判断
print('Please input your height and weight(without "and" calculate, and with conditions from the biggest number to the smallest number, and use less than operation)')
height = float(input('Input your height (centimeters):'))
weight = float(input('Input your weight (kilograms):'))
bmi = weight/((height/100)**2)
print(bmi)
if bmi>32:
    print('Extreme Obesity')
if bmi<= 32:
    print('Obese')
elif bmi<=28:
    print('over weight')
elif bmi<=25:
    print('healthy')
else:
    print('under weight')
#如果上述条件下使用and，则可以弥补错误
print('Please input your height and weight(without "and" calculate, and with conditions from the biggest number to the smallest number, and use less than operation)')
height = float(input('Input your height (centimeters):'))
weight = float(input('Input your weight (kilograms):'))
bmi = weight/((height/100)**2)
print(bmi)
if bmi>32:
    print('Extreme Obesity')
if bmi<= 32 and bmi>28:
    print('Obese')
elif bmi<=28 and bmi>25:
    print('over weight')
elif bmi<=25 and bmi>18.5:
    print('healthy')
else:
    print('under weight')





