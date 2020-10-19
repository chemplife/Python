'''
object: container that contains:
	-> data (state / attribute)
	-> functionality (behavior / methods)

Eg: my_car
	-> brand = Ferrari		-|
	-> model = 59xx			 |-> Attributes of 'my_car' Object
	-> price = 150000		 |
	-> year = 2015			-|
	-> accelerate			-|
	-> brake				 |-> methods / functionality of 'my_car' object
	-> steer				-|


Access Data or functionality:
	-> dot notation: my_car.brand
					my_car.year
					my_car.accelerate(10)
	-> getattr(Object_symbol, attribute_name, optional_default)


Assign Data / Attribute to an Object: This MUTATES the object 					*******************************
	-> setattr(Object_symbol, attribute_name, attribute_value)
	-> dot notation:
			object_symbol.attribute_name = attribute_value
** Won't work on Built-in objects, like int, str, etc

Delete Attribute from an Object: This MUTATES the object
	-> delattr(Object_symbol, attribute_name)
	-> del object_symbol.attribute_name
** Won't work on Built-in objects, like int, str, etc


How to create an Object / Container?
-> class keyword
	-> A class is like a template used to create an Object
		-> 'Template' is also called as 'Type'									*******************************
	-> Object created from a class is called instance of that class/type 		*******************************

##################
##################
# Classes are also Objects and have attributes and methods.
	-> Classes are 'Callable': my_car()
		-> Call to class returns an instance of class
			-> These instances are called as 'Objects' of class
			-> 'Type' of these objects is the 'class' they are created from.

# type(my_obj) -> 'My_Class'	<- 'My_Class' here is an Object (not a string) [classes are Objects]
# isinstance(my_obj, My_Class)	<- returns Boolean
# type(My_Class) -> type 		<- type of a class is 'type'

##################
##################

Where is the state / data stored?
	-> In a Dictionary
		-> This Dictionary is called as 'namespace'
		-> All 'Keys' in the namespace are 'Strings'.
		-> Python intern these Keys to find them quickly	(Intern: Add something to the Python cache [check interning.py])
		-> We CANNOT directly modify Class.__dict__, but we can read it. (it is not exactly a 'dict' type. It is a 'Hash Map')
		-> We CAN modify class_object.__dict__ ... (it is of type 'dict')


When we call a class (instantiate a class), it returns an object of type = Class_name
-> This class object has its own 'namespace'. It does NOT share namespace with the class. 			*******************************
-> But even if class_object.__dict__ = {} and ClassObject.__dict__ = {.., 'version': '3.7',...}
	-> class_object.version will return '3.7' ... Python when not find value for an assignment in the local namespace
		-> it goes one one level up, and in this case, look for 'varsion' value in the class's namespace

** Not all attributes of an Object in __dict__.. example, __name__, __class__ are not in __dict__

'''

class MyClass:
	pass

print(f'Type of class: {type(MyClass)}')
print('Attributes of Class like name: ',MyClass.__name__)

my_obj = MyClass()
print(f'Type of class object: {type(my_obj)}')
print('Attributes of Class like class: ',my_obj.__class__)

print('Is my_obj instance of MyClass?: ', isinstance(my_obj, MyClass))

# To Retrive an attribute of an Object
obj_class_attr = getattr(MyClass, '__name__')
class_obj_attr = getattr(my_obj, '__class__')
print(f'getattr for class:{obj_class_attr}\ngetattr for class obj:{class_obj_attr}')

print('\n\n---------------------- Get attributes ----------------------')
# dot notation way will give error, so we can use getattr()
class_obj_attr_default = getattr(my_obj, 'x', 'N/A')
print('Getting default value from getattr():', class_obj_attr_default)

print('All object data is stored in Dictionary:\n', MyClass.__dict__)

print('\n\n---------------------- Set attributes ----------------------')
# Set attribute
MyClass.version = '3.7'
setattr(MyClass, 'language', 'Python')

print('New Attribute 1:', getattr(MyClass, 'version', 'N/A'))
print('New Attribute 2:', MyClass.language)

MyClass.x = 100
print('New Attribute 3 in namespace:', MyClass.__dict__)

del MyClass.x
print('Attribute 3 deleted in namespace:', MyClass.__dict__)



print('\n\n---------------------------------- Set Setting Attribute Value to a Callable ----------------------------------')
'''
Setting Attribute Value to a Callable
'''
MyClass.say_hello = lambda : print('Hello World')

MyClass.__dict__['say_hello']()
MyClass.say_hello()
getattr(MyClass, 'say_hello')()


print('\n\n---------------------- namespace of class and class-object ----------------------')
print('Namespace of class:', MyClass.__dict__)
print('Namespace of class object:', my_obj.__dict__)

print('Value from namespace of class:', MyClass.version)
print('Value for class_object from namespace of class:', my_obj.version)

# Why we cannot modity __dict__ of a CLASS-Object, by we can modify it if it belongs to an instance of a class.
print('\nWe cannot modify namespace class dict. It is of type: ', type(MyClass.__dict__))
print('We can modify namespace class_object dict. It is of type: ', type(my_obj.__dict__))

print('\n\n---------------------- Function Attribute ----------------------')
'''
Function defined in a class will be a Class Method and is in the Class's namespace
MyClass.say_hello()			<function __main__.MyClass.say_hello()>

But for class instance (object of class)
my_obj.say_hello()			<Bound Method MyClass.say_hello of <__main__.MyClass at some_address_value>>
* This 'address_value' is pointing to the address of the instance object (my_obj).

Outputs of:
MyClass.say_hello()		-> 'Hello World'
my_obj.say_hello()		-> TypeError.. say_hello() takes 0 position arguments but 1 was given
# Why is that?

'Method' - Actual Object Type
	-> LIKE a function (So it is callable)
	-> UNLIKE a function, when a method is called, it is BOUND to some object.
		-> That Object is passed as the '1st Parameter' of the method.
	-> They combine an instance of class and a function defined in the class.
	-> Like any object it has attributes, and Python provides some attributes too.
		-> __self__ : Instance to which the method is bound to.
		-> __func__ : points to the Original function that is defined in the class.
			-> Eg: obj.method(args) -> method.__func__(method.__self__, arg)

So,
	my_obj.say_hello()		: say_hello() is a method object, which is bound to 'my_obj'
		-> when the above method is called, it took 'my_obj' as its '1st parameter'.
	meaning?
		-> my_obj.say_hello() == MyClass.say_hello(my_obj)

	How to use the functions bound to an instance?
		-> using 'self' as one argument in the function definition.
			-> def say_hello(self):
	

** When a function is defined in the Class, it is just an 'instance function'.
** When a function is called using an instance object, it is now, an 'instance method'. Because, now it is bound to an object
	-> type(my_obj.say_hello) is type(MyClass.say_hello) : False

## Advantage:
Since, 'method objects' (like say_hello()) takes an object (like my_obj) as a parameter
	-> They have handle over the namespace of the passed object.

# Function in the namespace of the instance-object are not the Bound-Methods.
'''

class MyClass:
	def say_hello():
		pass

print('Is instance function same as instance method?:',type(my_obj.say_hello) is type(MyClass.say_hello))
print('Class function is :', type(MyClass.say_hello))
print('Class-object function is :',type(my_obj.say_hello))

print('\n')

# 'self' is just a name put aside for 'instance_object'
# here, 'instance_obj' == 'self' 
class Person:
	def set_val(instance_obj, new_name):
		instance_obj.name = new_name

p1 = Person()

p1.set_val('Alex')
print('namespace of p1:', p1.__dict__)

p2 = Person()

Person.set_val(p2, 'John')
print('namespace of p2:', p2.__dict__)

p3 = Person()
m_hello = p3.set_val

print('Method say_hello() :', m_hello)
print(f'Attributes of instance-method: m_hello.__self__ = {m_hello.__self__}\n\t\t\t\t\t\t\t   m_hello.__func__ = {m_hello.__func__}')

p2.my_func = lambda: 'Instance-object function called..'
print('Not a Bound-Method: ', p2.my_func,'\nThe namespace of class-object:', p2.__dict__)
print("Not a Bound-Method called without 'self':", p2.my_func())


'''
Monkey Patching: Modefying the attributes of a class or an object at runtime

'''
print('\n\n---------------------- Monkey Patching ----------------------')
class People:
	def say_hello(self):
		print(f'Instance-method called by object: {self}')

p = People()
print('Instance-method say_hello():', p.say_hello)

People.do_work = lambda self: print(f'Do-work instance method by object:', self)
# Here the class is Monkey Patched. We don't have to recreate our object 'p'
# When Python doesn't find the function/attribute in the namespace of the instance,
# it looks into the namespace of the class and finds the function there.
print('Instance-method do_work:', p.do_work)


print('\n\n---------------------------------- Initializing Class Instance ----------------------------------')
'''
When a class is 'instantiated':
	-> A New instance of the class is created
	-> Namespace of the class-object is initialized.. to {} (depends on __init__())

We can provide our custom initializer method that will get called when class in 'Instantiated'
	-> def __init__(obj, version):
	-> It works as a 'Bound Method'
	-> Eg: MyClass('3.7')
		-> creates new instance with an empty namespace for it.
		-> __init__() if defined will
			-> obj.__init__('3.7') == MyClass.__init__(obj, '3.7')
			-> Here 'version' will be an 'Instance-Object' attribute, and will be in "Instance-object's" namespace 		**********

** By the time __init__() is called, Python has already created the Instance-Object
	-> And the Instance-Object's namespace (__dict__) is already intialized to {}

__new__() : This method creates a new Instance-Object and Initialize the namespace to {}.
	-> We can create the Instance-Object in a custom way.
'''

class Person:
	def __init__(self):
		print('Initializing statement..')

# This will print the __init__() print statement
p = Person()

class Person:
	def __init__(self, name):
		self.name = name

# This will print the __init__() print statement
p = Person('Eric')
print('Namespace of Instance-Object:', p.__dict__)


print('\n\n------------ Creating and binding method to an instance at runtime ------------')
'''
This lets us create a Bound-Method that is only available to 1 object of the class.
Other Class object won't be able to use it.
'''

from types import MethodType
# MethodType(function, object)

class People:
	language = 'Python'

p2 = People()
p3 = People()
# Have to assign 'MethodType' to an attribute of 'p1' object to have it in the object's Namespace.
# Here 'my_func' is created for that.
p2.my_func = MethodType(lambda self: f'Hello {self.language}', p2)
print('P2 Bound-Method:', p2.my_func,'\nP2 Namespace:', p2.__dict__)
print('P2 Call Bound-Method:', p2.my_func())
print('P3 Namespace:', p3.__dict__)

print('\n\n------------ Creating Bound-Methods custom to each Instance within class ------------')

class Person:
	def __init__(self, name):
		self.name = name

	def register_do_work(self, func):
		setattr(self, '_do_work', MethodType(func, self))

	def do_work(self):
		# We can use Dot Notation, but if this function is called before 'register_do_work', it will raise error.
		# getattr() provides a 'Default Value' in case the function/attribute does not exist.
		do_work_method = getattr(self, '_do_work', None)

		if do_work_method:
			return do_work_method()

		else:
			raise AttributeError('You must Run register_do_work()')

p1 = Person('Eric')
p2 = Person('John')

# Now, this won't work, even if the method is defined in the class.
# p1.do_work()

def p1_method(self):
	return f'{self.name} will be here'

p1.register_do_work(p1_method)
print('P1 namespace:', p1.__dict__)

# Now, this will work for 'p1'
print('p1 Bound method: ',p1.do_work)
print('p1 Bound method called: ',p1.do_work())

# Something different for P2
def p2_method(self):
	return f'{self.name} is in London sipping tea..'

p2.register_do_work(p2_method)
print('\nP2 namespace:', p2.__dict__)

# Now, this will work for 'p1'
print('p2 Bound method: ',p2.do_work)
print('p2 Bound method called: ',p2.do_work())

print('\n')

# Usage Example
people = [p1, p2]
for p in people:
	print(f'For Loop do_work call. {p}: ', p.do_work())