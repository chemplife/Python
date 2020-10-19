'''
Class-Bound-Functions:
It is possible to create functions that are 'Bound' to the 'Class', no matter how they are called.
Eg:
	-> MyClass.fn 			|-> In both these cases, the function 'fn' is nver going to be Bound to the instance.
	-> m.fn 				|->		'fn' needs to be Bound to Class howsoever it is called.

@classmethod
How, it works is in Metaprogramming part.


Static-Functions:
It is possible to have functions that will never be bound to any object when called

@staticmethod


Summary:
instance-bound-function: receives instance object as their 1st Argument.
	-> Access instance info: self.attribute_name
class-bound-function: receives class as their 1st Argument.
	-> Access class info: cls.attribute_name
static-function: No argument received as thet are not bound to anything.
	-> Access Class info: Class_Name.attribute_name
'''

# Class-Bound-Functions and 
# Static-Functions:
class MyClass:
	def hello():
		print('Hello!')

	def inst_hello(self):
		print(f'Hello from Instance {self}..')

	@staticmethod
	def help():
		return 'Help Available'

	@classmethod
	def cls_hello(cls):
		print(f'Hello from Class {cls}')

c = MyClass()

#Type of help() = Function.		-> It is not bound to anything
print('--------------------------- Static-Functions ---------------------------')
print('Class Call-> Type of function help(): ', type(MyClass.help))
print('Class-> Help Call: ', MyClass.help())
print('Class-Object Call-> Type of function help(): ', type(c.help))
print('Class-Object-> Help Call: ', c.help())

print('\n\n--------------------------- Class-Bound-Functions ---------------------------')
print('Class Call-> Type of function cls_hello: ', type(MyClass.cls_hello))
print('Class-> cls_hello Call: ', MyClass.cls_hello())
print('Class-Object Call-> Type of function cls_hello: ', type(c.cls_hello))
print('Class-Object-> cls_hello Call: ', c.cls_hello())

print('\n\n--------------------------- Functions Scopes ---------------------------')
'''
Anything inside a class is in the local-scope of the class.
Except the Functions.
Any function defined in the class is in global Namespace.
'''

def full_version():
	return f'{Languages.MAJOR}.{Languages.MINOR}.{Languages.REVISION}'

class Languages:
	MAJOR = 3
	MINOR = 7
	REVISION = 4

	full_version = full_version

	@property
	def version(self):
		return f'{self.MAJOR}.{self.MINOR}.{self.REVISION}'

	@classmethod
	def cls_version(cls):
		return f'{cls.MAJOR}.{cls.MINOR}.{cls.REVISION}'

	@staticmethod
	def static_version():
		return f'{Languages.MAJOR}.{Languages.MINOR}.{Languages.REVISION}'
	
l = Languages()
print('Class-Object version: ', l.version)
print('ClassMethod version: ', Languages.cls_version())
print('ClassMethod version from Class-Object: ', l.cls_version())
print('StaticMethod version: ', Languages.static_version())
print('Is Languages.full_version same as full_version?: ', Languages.full_version is full_version)
print('Outside function called the same way as staticmethod: ', Languages.full_version)

# Example 2
# Remember: Function definitions are Global in nature..

print('\n')

name = 'Mickey'

class Person:
	name = 'Mouse'
	list_1 = [name]*3
	list_2 = [name for i in range(3)]

	@classmethod
	def hello(cls):
		return f"'{name}' says Hello"

#This will take 'name' from global scope.
print('Class Call:', Person.hello())

# Within the class, name is local
print('List1:', Person.list_1)

# List Comprehensions are of type 'functions'.. Hence Global Scope.. VERY IMPORTANT..
print('List2:', Person.list_2)