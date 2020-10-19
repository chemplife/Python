'''
MetaClass: A class that us used to create other classes.

In 'class_creation.py', we were doing everything Manually..
	-> Creating class_body, class_dict, executing the class_body in the class_dict,
		then passing everything to the MetaClass to create the class..

By default, Python uses 'type' class to create other classes and thus 'type' is a MetaClass...
We basically want Python to use our Custom Class to be used for creating other classes..
And we can override the default behavior to do that..
	
	-> class MyClass(metaclass=MyType)

Eg:
	class MyType(type):
		def __new__(mcls, name, bases, cls_dict):

			# tweak things here..

			# Create class via delegation
			new_class = super().__new__(mcls, name, bases, cls_dict)

			# tweak some more..

			# and return the new_class
			return new_class

	class Person(metaclass=MyType):
		def __init__(self, name):
			self.name = name

	Here:
	-> mcls = MyType	('MyType' is the class mentioned as Metaclass)
	-> name = Person	('Person' class is the class that invoked the 'MyType' Metaclass)
	-> bases = object	(since Person class is not inheriting from any other class)
	-> cls_dict 		('class' keyword will take care of the 'class_dict' creation, and executing 'class_body' in it )
						('class' Keyword will take care of calling MyType(class_name, class_base, class_dict) as well..)
'''

class Person:
	pass

class Point(metaclass=type):
	pass

print('Types of Person and Point classes: ', type(Person), ',', type(Point))

print('\n')

class CustomType(type):
	def __new__(mcls, name, bases, cls_dict):
		print(f"Using Custom metaclass: '{mcls.__name__}', to create class: '{name}', inherited from: '{bases}'")
		cls_obj = super().__new__(mcls, name, bases, cls_dict)
		cls_obj.area = lambda self: self.l * self.b
		return cls_obj

class Rectangle(Point, metaclass=CustomType):
	def __init__(self, l, b):
		self.l = l
		self.b = b

	def circ(self):
		return 2 * self.l * self.b

rec = Rectangle(10,20)
# We injected 'area()' method into the class at the time of class creation (technically right after the class creation)..
print('Area of Rectangle:\t\t\t', rec.area())
print('Circumference of Rectangle: ', rec.circ())