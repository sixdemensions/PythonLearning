# To call a function, you need to know the name and parameters of the function. For example,
# the absolute value function abs has only one parameter. 
# You can view the documentation directly from Python's official website, 
# or you can view the help information of the abs function through help(abs) on the interactive command line.
a = -100
print(abs(a))
#The max function max() can receive any number of parameters and return the largest one:
a = max(1,2)
print(a)
# Commonly used built-in functions in Python also include data type conversion functions. For example, the int() function can convert other data types into integers:
a = int('123')
print(a)

a = float('12.23')
print(a)

a = str(12.12)
print(a)

a = bool(1)
print(a)

a = bool(0)
print(a)