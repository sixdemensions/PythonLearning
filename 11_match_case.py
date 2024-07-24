#当我们用if ... elif ... elif ... else ...判断时，会写很长一串代码，可读性较差。
#如果要针对某个变量匹配若干种情况，可以使用match语句
#match语句除了可以匹配简单的单个值外，还可以匹配多个值、匹配一定范围，并且把匹配后的值绑定到变量：
#在这个示例中，第一个case x if x < 10表示当age < 10成立时匹配，且赋值给变量x，第二个case 10仅匹配单个值，第三个case 11|12|...|18能匹配多个值，用|分隔。
age = int(input())
match age:
    case a if a < 10:
        print(f'< 10 years old: {a}')
    case 10:
        print('10 years old.')
    case 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18:
        print('11~18 years old.')
    case 19:
        print('19 years old.')
    case _:
        print('not sure.')

