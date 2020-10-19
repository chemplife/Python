'''
When Python sees

	class Person:
		planet = 'Earth'
		name = property(fget = lambda self: self._name)

		def __init__(self, name):
			sefl._name = name

it adds 'Person' in the namespace of the code, and it refers to 'class Person'.. basically, it is an object

There is a class called 'type'
	-> Classes are instances of class 'type'
	-> that is why, classes are also called as 'types'
	-> since 'type' is callable, therefor classes are callables too.
	
	** since 'type' is a class, it inherits from 'object class'

Steps of creating a class:
1. The class body is extracted like a blob of text..
2. A dictionary is created to hold the namespace of the class
3. class body is executed inside the created namespace.
	-> this populates the namespace with all the things we have in class
4. A new 'type' instance is created using the name of the class, the base-class, and populated namespace-dictionary
	-> type(class_name, base_class, class_dict)
		-> class_name: Person
		-> base_class: object class (we did not inherit from any class in particular)
		-> class_dict: Person.__dict__

So, like calling a class creates an instance of the class:		p = Person()		-> 'p' is the instance of class Person
Similarly, when we call 'type' with class_name, base_class, and class_dict
	-> it creates an instance of class 'type'
		-> name of the instance => class_name
		-> Any inheritance		=> base_class
		-> instance namespace 	=> class_dict

	** 'type' takes an executed code's namespace as parameter and not the code itself..
		so, we need to execute the 'text blob' of code first because calling type()..

** Since type() class creates more classes.. it is a kind of MetaClass..
'''
print('------------------------------------- Python Creating Class -------------------------------------\n')

import math

class Circle(object):
	def __init__(self, x, y, r):
		self.x = x
		self.y = y
		self.r = r

	def area(self):
		return math.pi * self.r**2

print('Class name in the global namespace?: ', 'Circle' in globals())
print('Type of class Circle: ', type(Circle).__name__)


print('\n\n------------------------------------- Creating Class Manually -------------------------------------\n')


# Step 1: Class_name
class_name = 'Circle'

# Step 1: Class_body
class_body = '''
def __init__(self, x, y, r):
		self.x = x
		self.y = y
		self.r = r

def area(self):
	return math.pi * self.r**2
'''

# Step 1: class_bases.. since we are only using object-class.. we can keep it empty.
class_bases = ()

# Step 2: Class_dict
namespace = {}

# Step 3: executing class_body
exec(class_body, globals(), namespace)
print('namespace to use for our class creation: ', namespace)

# Step 4: Calling 'type' class
Circle = type(class_name, class_bases, namespace)
print('\nType of type-instance -> Circle: ', type(Circle))
print('\nDictionary of type-instance -> Circle:', Circle.__dict__)
print('\nName of type-instance -> Circle: ', Circle.__name__)

# Now, we can create instances of 'Circle' as well because it is of type 'type'

c = Circle(0,0,1)
print('\nType of Circle-instance: ', type(c))
print('\nDictionary of type-instance -> Circle:', Circle.__dict__)
print('\nArea of this instance: ', c.area())


print("\n\n------------------------------------- Inheriting from 'type' class -------------------------------------\n")
'''
Since, 'type' is a class, we can inherit our custom class from 'type' class.
-> We can override the __new__() method.. tweak some things in our custom class.. and ask 'type' to create an instance for us..
	-> this instance returned by 'type' will be of type 'type'.. and class is of type 'type'..
		-> we created a custom types..
	
	We bascially intercepted the 'Creation-of-Class'..
	THAT IS METACLASS.. and are doing METAPROGRAMMING..
'''
class Test:
	def __new__(cls, *args, **kwargs):
		print(f"New instance of '{cls}' is created. It has arguments: {args} and {kwargs}")

t = Test(10, 20, a= 4, b=5)
t = Test.__new__(Test, 10, 20, a= 4, b=5)

print('\n------------ Custom Type to create Classes ------------\n')

# This is a METACLASS.. we can do customized creation of classes..
class CustomType(type):
	def __new__(cls, name, bases, class_dict):
		print("Customized 'type' Creation!!")
		# This will do the same as line 127 is doing..
		# here we are adding to class_dict before creating the class..
		#class_dict['circ'] = lambda self: 2 * math.pi * self.r
		cls_obj = super().__new__(cls, name, bases, class_dict)
		# here we are adding to class_dict after creating the class..
		cls_obj.circ = lambda self: 2 * math.pi * self.r
		return cls_obj


class_body = '''
def __init__(self, x, y, r):
		self.x = x
		self.y = y
		self.r = r

def area(self):
	return math.pi * self.r**2
'''

class_dict = {}

exec(class_body, globals(), class_dict)
print('namespace to use for our class creation: ', class_dict)

Circle = CustomType('Circle', (), class_dict)
print('Type of type-instance -> Circle: ', type(Circle))
print('Dictionary of type-instance -> Circle:', Circle.__dict__)
print('Name of type-instance -> Circle: ', Circle.__name__)

# Now, we can create instances of 'Circle' as well because it is of type 'type'

c = Circle(0,0,1)
print('\nType of Circle-instance: ', type(c))
print('Dictionary of type-instance -> Circle:', Circle.__dict__)
print('Area of this instance: ', c.area())
print('Circumference of this instance: ', c.circ())