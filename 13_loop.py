#Python的循环有两种，一种是for...in循环，依次把list或tuple中的每个元素迭代出来
#执行这段代码，会依次打印names的每一个元素：
#所以for x in ...循环就是把每个元素代入变量x，然后执行缩进块(indented block)的语句。
names = ['Micheal','Bob','Tracy']
for name in names:
    print(name)
#比如我们想计算1-10的整数之和，可以用一个sum变量做累加：
sum = 0#调用一个名为 sum 的变量，并将其赋值为0。这通常用作在循环或一系列运算中累计总数的起点。
for x in [1,2,3,4,5,6,7,8,9,10]:
    sum = sum+x
print(sum) 
#如果要计算1-100的整数之和,range()函数，可以生成一个整数序列，再通过list()函数可以转换为list。比如range(5)生成的序列是从0开始小于5的整数：
sum = 0
for x in range(101):
    sum = sum + x
print(sum)
#第二种循环是while循环，只要条件满足，就不断循环，条件不满足时退出循环。比如我们要计算100以内所有奇数之和，可以用while循环实现：
sum = 0
n = 99
while n > 0:
    sum = sum + n
    n = n -2 #在循环内部变量n不断自减，直到变为-1时，不再满足while条件，循环退出。
print(sum)
#练习利用循环依次对list中的每个名字打印出Hello, xxx!：
L = ['Bart','Lisa','Adam']
for name in L:
    print(name)
#In a loop, the break statement can exit the loop early. For example, the numbers 1 to 100 that would have been printed cyclically:
n = 0
while n <= 100:
    print(n)
    n = n + 1
print('END')
#If you want to end the loop early, you can use the break statement:
n = 0
while n <= 100:
    if n > 10:
        break
    print(n)
    n = n +1
print('END')
#During the loop, you can also use the continue statement to skip the current loop and start the next loop directly.
n = 0
while n <= 10:
    n = n + 1
    if n%2 == 0: # If n is an even number, exctute the continue statement
        continue # The continue statement will continue the next loop directly, and the subserquet print() statement will not be excuted
    print (n)

# When you execute the above code, you can see that the numbers printed are no longer 1 to 10, but 1, 3, 5, 7, and 9.
# It can be seen that the function of continue is to end the current cycle early and start the next cycle directly.


##In Python and many other programming languages, the expression n % 2 == 0 is used to determine if a number n is even. Here's why this works:

# % (Modulo Operator): In Python, the % operator computes the remainder of dividing n by 2.
# Even Numbers: By definition, an even number is divisible by 2 with no remainder.
# When you write n % 2 == 0, you are checking:
# n % 2: This computes the remainder when n is divided by 2.
# == 0: This checks if the remainder is equal to 0.
# Therefore, if n % 2 == 0 evaluates to True, it means that n is perfectly divisible by 2 (there is no remainder), indicating that n is an even number.
# Conversely, if n % 2 != 0 (meaning the remainder is not zero), then n is an odd number because it cannot be perfectly divided by 2 without leaving a remainder.
# This method is efficient and commonly used in programming to distinguish between even and odd numbers based on their divisibility by 2.

