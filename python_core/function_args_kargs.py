# *args scoops the positional arguments into a Tuple.
# **kwargs scoops the Keyword arguments into a Dictionary.

def my_func0(a,b,*args):
	print('my_func0')
	print(f'a:{a}, b:{b}, args:{args}')

my_func0(10,20,30,40)
print('-------------------------------')

# '*args' takes all the left overs.
# To have anything after'*args', it needs to be Keyword
def my_func1(a,b,*args, d):
	print('my_func1')
	print(f'a:{a}, b:{b}, args:{args}, d:{d}')

my_func1(10,20,30,40, d=50)
print('-------------------------------')

# To stop any positional arguments, use '*'
# '*' means, no positional arguments after that.
def my_func2(e,f,*, a,b,d):
	print('my_func2')
	print(f'e:{e}, f:{f}, a:{a}, b:{b}, d:{d}')

my_func2(5,1,a=10,b=20,d=50)
print('-------------------------------')

# No Argument can come after **kwargs
def my_func3(*,a,**kwargs):
	print('my_func3')
	print(f'a:{a}, kwargs:{kwargs}')

my_func3(a=10,b=20,d=50)
print('-------------------------------')


def my_func4(e,f,*args,a,**kwargs):
	print('my_func4')
	print(f'e:{e}, f:{f}, args:{args}, a:{a}, kwargs:{kwargs}')

my_func4(5,1,4,5,6,a=10,b=20,d=50)
print('-------------------------------')


def my_func5(*args,**kwargs):
	print('my_func5')
	print(f'args:{args},kwargs:{kwargs}')

my_func5(5,1,4,5,6,a=10,b=20,d=50)
print('-------------------------------')


# args and kwargs can be empty
def my_func6(*args,**kwargs):
	print('my_func6')
	print(f'args:{args},kwargs:{kwargs}')

my_func6()
print('-------------------------------')