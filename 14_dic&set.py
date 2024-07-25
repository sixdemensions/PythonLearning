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