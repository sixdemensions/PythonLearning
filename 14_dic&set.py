# Python has built-in dictionary support: dict. The full name of dict is dictionary. It is also called map in other languages. It uses key-value (key-value) storage and has extremely fast search speed.
names = ['Miacheal','Bob','Tracy']
Score = [95,75,85]
print(names[0],Score[0])
# If you use dict to implement it, you only need a "name"-"score" comparison table, and you can search for scores directly based on the name. No matter how big the table is, the search speed will not slow down. Write a dict in Python as follows:
d = {'Micheal':95,'Bob':75,'Tracy':85}
print(d['Micheal'])
# The method of putting data into dict, in addition to specifying it during initialization, can also be put in by key:
d['Adam'] = 67
print(d['Adam'])
# Since a key can only correspond to one value, if you put value into a key multiple times, the subsequent value will flush out the previous value:
d["Jack"] = 90
print(d['Jack'])
d['Jack'] = 88
print(d['Jack'])
# If the key does not exist, dict will report an error:
# print(d['Thomas'])
# To avoid the error that the key does not exist, there are two ways. One is to use in to determine whether the key exists:
if 'Thomas' in d:
    print('True')
else:
    print('False')
# The second is through the get() method provided by dict. If the key does not exist, you can return None or the value you specify:
d.get('Thomas',-1) # works only in python interactive enviroment
# To delete a key, use the pop(key) method, and the corresponding value will also be deleted from the dict:
d.pop('Bob') 
d # works only in python interactive environment
print(d)
#正确使用dict非常重要，需要牢记的第一条就是dict的key必须是不可变对象
#要保证hash的正确性，作为key的对象就不能变。在Python中，字符串、整数等都是不可变的，因此，可以放心地作为key。而list是可变的，就不能作为key
# test
# Set is similar to dict, it is also a collection of keys, but does not store values. Since keys cannot be repeated, there are no duplicate keys in the set.
# To create a set, list each element using {x,y,z,...} :
s = {1,2,3}
print(s)
# Or provide a list as the input collection:
s = set([1,2,3])
print(s)
# Note that the parameter [1, 2, 3] passed in is a list, and the displayed {1, 2, 3} only tells you that there are 3 elements 1, 2, and 3 inside the set, and the order of display does not indicate it. set is ordered. 

# Duplicate elements are automatically filtered in the set:
s = {1,2,3,4,5,1,2,3}
print(s)

# Elements can be added to the set through the add(key) method. It can be added repeatedly, but it will have no effect:
s.add(6)
print(s)

#A set can be regarded as a collection of unordered and non-repeating elements in the mathematical sense. Therefore, two sets can perform operations such as intersection and union in the mathematical sense:
s1 = {1,2,3}
s2 = {3,4,5}
print(s1 & s2) # intersection operation "&"
print(s1 | s2) # union operation "|"

#As we said above, str is an immutable object, while list is a mutable object.
#For mutable objects, such as lists, the contents inside the list will change when the list is operated on, for example:
a = ['c','b','a']
a.sort()
print(a)
# For immutable objects, such as str, how to operate on str:
a = 'abc'
a.replace('a','A')
print(a) #虽然字符串有个replace()方法，也确实变出了'Abc'(在命令行中)，但变量a最后仍是'abc'，应该怎么理解呢？

# Let’s first change the code to the following:
a = 'abc'
b = a.replace('a','A')
print(b)

# 要始终牢记的是，a是变量，而'abc'才是字符串对象！有些时候，我们经常说，对象a的内容是'abc'，但其实是指，a本身是一个变量，它指向的对象的内容才是'abc'：
# 当我们调用a.replace('a', 'A')时，实际上调用方法replace是作用在字符串对象'abc'上的，而这个方法虽然名字叫replace，但却没有改变字符串'abc'的内容。相反，replace方法创建了一个新字符串'Abc'并返回，如果我们用变量b指向该新字符串，就容易理解了，变量a仍指向原有的字符串'abc'，但变量b却指向新字符串'Abc'了：
# 所以，对于不变对象来说，调用对象自身的任意方法，也不会改变该对象自身的内容。相反，这些方法会创建新的对象并返回，这样，就保证了不可变对象本身永远是不可变的。