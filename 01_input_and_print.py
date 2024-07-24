#Python learing basic 01
#输入和输出
##用print()在括号中加上字符串，就可以向屏幕上输出指定的文字。
print('hello world')
##print()函数也可以接受多个字符串，用逗号“,”隔开，就可以连成一串输出：
print('the quick brown fox','jump over','the lazy dog')
##print()也可以打印整数，或者计算结果：
print(300)
print(100 + 200)
print('100 + 200 =',100+200)
##Python提供了一个input()，可以让用户输入字符串，并存放到一个变量里。比如输入用户的名字：
###此时运行calc.py不能正确执行，需要调用python交互式命令行，输入以下代码。
name = input()
###添加print命令后可实现正确执行
print(name)
