import inspect

#TODO: Fix this function
#To it as we go
def myfunc(a,b:int=1, c:'str'='abc',*args,y:int, z:float=1.013, **kwargs) -> float:
	'''This is a test function to see all the attributes related to a function.'''
	i = 0
	pass

myfunc.category = 'math'
myfunc.subcategory = 'arithmetic'
# print all attributes
print(dir(myfunc))

print('-------------------------------')
# Print all annotations
print(myfunc.__annotations__)

print('-------------------------------')
# Print all doc_strings
print(myfunc.__doc__)

print('-------------------------------')
# Print all default non-keyword parameters
print(myfunc.__defaults__)

print('-------------------------------')
# Print all default keyword parameters
print(myfunc.__kwdefaults__)

print('-------------------------------')
# Print name of the function
print(myfunc.__name__)

print('-------------------------------')
# __Code__ has its own properties.
#get list of all variables of the function
print(myfunc.__code__.co_varnames)
#get all positional arguments of the function
print(myfunc.__code__.co_argcount)
print(dir(myfunc.__code__))

print('-------------------------------')
print('-------------------------------')
print('\nINSPECT SECTION\n')
#functions are independent from a class
print(inspect.isfunction(myfunc))
#method is related to a class.
print(inspect.ismethod(myfunc))
#both method and functions are routine
print(inspect.isroutine(myfunc))
#get sourcecode of the function
print(inspect.getsource(myfunc))
#where is the functiuon defined.
print(inspect.getmodule(myfunc))
#get TODOs for the function. Basically any comment right before the function
print(inspect.getcomments(myfunc))
print('-------------------------------')
print('SIGNATURE\n')
sig = inspect.signature(myfunc)
for params in sig.parameters.values():
	print('Name:', params.name)
	print('Default:', params.default)
	print('Annotation:', params.annotation)
	print('Kind:', params.kind)
	print('--------------')
# '__call__',
# '__class__',
# '__closure__',
# '__delattr__',
# '__dict__',
# '__dir__',
# '__eq__',
# '__format__',
# '__ge__',
# '__get__',
# '__getattribute__',
# '__globals__',
# '__gt__',
# '__hash__',
# '__init__',
# '__init_subclass__',
# '__le__',
# '__lt__',
# '__module__',
# '__ne__',
# '__new__',
# '__qualname__',
# '__reduce__',
# '__reduce_ex__',
# '__repr__',
# '__setattr__',
# '__sizeof__',
# '__str__',
# '__subclasshook__',
# 'category',
# 'subcategory'



