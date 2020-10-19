'''
__new__() is a method of 'object class' from which every class inherites functionality by default.
(Everything is an object of a class, and super-class of every class is the 'object-class')
	
	->__new__ creates the instance of a class.
	-> __init__() is called after the object/instance is created.
		-> (this happens when instance is created using class-name. Because in essence, we are calling the class, which runs __init__..)
		-> But if we call the __new__() directly from object, the __init__ will not run unless we call it.
'''

class Person:
	def __init__(self, name):
		self.name = name

# Calling __new__() directly from 'object-class'
p = object.__new__(Person)
print('P __dict__ : ', p.__dict__)

# Since we called __new__() directly, __init__() needs to be called directly too.
p.__init__('Guido')

p2 = Person('Raymond')
print('P2 __dict__: ', p2.__dict__)

print('\nType of object p : ', type(p))
print('Type of object p2: ', type(p2))


'''
object.__new__(class, *args, **kwargs)
	-> it is a STATIC method
	-> class: is the class for which we want to create the instance/object of.
	-> accepts *args and **kwargs: But it ignores all these arguments..
	-> signature must match __init__ of the class 	(def __new__(a,b,c), then __init__(a,b,c).. cannot be anything else..)
	-> Returns a new object of type-class

	** Our custom __new__ must follow the above rules.
		-> Should return a new object of the class __new__ belongs to.
			-> If __new__ returns object of some other type-class, __init__ won't run by itself.
		
		Why would we override __new__() if it is just creating the instance of the class?
		-> To do something before or after instance creation and definitely before __init__()
		-> it is wise to deligate the actual 'instance-creation' part back to Python.
			-> super().__new__	(to make inheritance work properly.)
			-> object.__new__	(will bypass any Parent class __new__ and go directly to 'object-class')

	p = Person('Guido') ==> Python calls '__new__(Person, 'Guido')' and returns cls_object.
						==> if isinstance(cls_object, Person)
							-> cls_object.__init__('Guido')

	** This is why, if isinstance(cls_object, Person) is 'False'
		-> Python won't know that whatever class 'cls_object' is an instance of accepts the same Parameters as 'Person' class's __init__ do..
		-> So, it will let us call the proper __init__()
'''
print('\n')

# We can override __new__() even when we inherit from Built-in types..
# which does not work with __init__().. But it is more of a part of 'Abstract Base Classes'..
# Just for example..
class Squared(int):
	def __new__(cls, x):
		# We can change the internal state of the argument making call to a built-in method here..
		return super().__new__(cls, x**2)

s = Squared(4)
print('Type of s: ', type(s))
print('Is s if instance int?: ', isinstance(s, int))
print('Value of s: ', s)

print('\n')

# But this won't work.. and we can't change the internal state of the argument here..
# Not all Built-In methods support it.
class Squared(int):
	def __init__(self, x):
		print('Calling init..')
		super().__init__(x**2)

try:
	s1 = Squared(4)
except TypeError as ex:
	print('Exception happened:', ex)


print('\n\n---------------------------- Example what we can do with __new__ ----------------------------\n')

class Square:
	def __new__(cls, w, l):
		cls.area = lambda self: self.w * self.l
		instance = super().__new__(cls)
		return instance

	def __init__(self, w, l):
		self.w = w
		self.l = l

sq = Square(3,4)
# We created area() as a class-method while creating the instance of the class.
# We injected a function in the class before creating it..
print('Area with __init__   : ', sq.area())

# And we don't even need __init__, in this case..
class Square:
	def __new__(cls, w, l):
		cls.area = lambda self: self.w * self.l
		instance = super().__new__(cls)
		instance.w = w
		instance.l = l
		return instance

sq = Square(3,4)
# We created area() as a class-method while creating the instance of the class.
# We injected a function in the class before creating it..
print('Area without __init__: ', sq.area())

print('\n\n---------------------------- __init__ not called if __new__ returns different instance ----------------------------\n')

class Person:
	def __new__(cls, name):
		print('Creating instance of other than Person-Class..')
		instance = str(name)
		return instance

	def __init__(self, name):
		print('init called..')
		self.name = name

p = Person('Alex')
# print from __init__() will not show up..
print('Type of object p: ', type(p))
# this will throw error, as str() does not have __dict__
# print('P __dict__: ', p.__dict__)