#以f开头的字符串，称之为f-string，它和普通字符串不同之处在于，字符串如果包含{xxx}，就会以对应的变量替换
#**为幂指数，变量:.2f为显示几位小数
r = 2.5
s = 3.14 * r ** 2
print(f'The area of a circle with radius {r} is {s:.2f}')
#占位符	替换内容 %d	整数 %f	浮点数 %s	字符串 %x	十六进制整数
print('%2d-%02d' % (3, 1))
print('%.2f' % 3.1415926)
# -*- coding: utf-8 -*-
s1 = float(input('请输入小明去年的中考成绩：'))
s2 = float(input('请输入小明今年的中考成绩：'))
r = (s2-s1)/s1*100
print(f'小明的成绩今年提升了{r:.2f}%' )