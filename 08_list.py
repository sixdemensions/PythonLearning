#Python内置的一种数据类型是列表：list。list是一种有序的集合，可以随时添加和删除其中的元素。
classmates = ['Micheal','Bob','Tracy']
print(classmates)
#变量classmates就是一个list。用len()函数可以获得list元素的个数：
print(len(classmates))
#用索引来访问list中每一个位置的元素，记得索引是从0开始的：
print(classmates[0])
#如果要取最后一个元素，除了计算索引位置外，还可以用-1做索引，直接获取最后一个元素：
print(classmates[-2])
#list是一个可变的有序表，所以，可以往list中追加元素到末尾：
classmates.append('Adam')
print(classmates[-1])
print(classmates[-2])
#也可以把元素插入到指定的位置，比如索引号为0的位置：
classmates.insert(0,'Jack')
print(classmates[0])
#要删除指定位置的元素，用pop(i)方法，其中i是索引位置：
classmates.pop(0)
print(classmates[0])
#要把某个元素替换成别的元素，可以直接赋值给对应的索引位置：
classmates[0] = 'Sarah'
print(classmates[0])
#list里面的元素的数据类型也可以不同，比如：
L = ['Apple',123,True]
#list元素也可以是另一个list，比如：
S = ['Python','Java',['asp','php'],'Scheme']
#要注意s只有4个元素，其中s[2]又是一个list，如果拆开写就更容易理解了：
p = ['asp','php']
s = ['Python','Java',p,'Scheme']
#要拿到'php'可以写p[1]或者s[2][1]，因此s可以看成是一个二维数组
print(p[1])
print(s[2][1])
#另一种有序列表叫元组：tuple。tuple和list非常类似，但是tuple一旦初始化就不能修改，比如同样是列出同学的名字：
classmates = ('Micheal','Bob','Tracy')
print(classmates)
#只有1个元素的tuple定义时必须加一个逗号,，来消除歧义：
t = (1,2)
print(t)
t = (1,)
print(t)
L = [
    ['Apple','Google','Microsoft'],
    ['Java','Python','Ruby','PHP'],
    ['Adam','Bart','Lisa']
]
# 打印Apple:
print(L[0][0])
# 打印Python:
print(L[1][1])
# 打印Lisa:
print(L[2][2])
