'''
type:		tells the class the object is created from. It does not take into account the inheritance of the class itself.
isinstance:	takes into account the inheritance of the object.

Every Class inherits functionalities from a common 'object' class. (it is not 'Object' because it is written in 'C' and classes in 'C' does
	not follow Camel casing.. eg. int(), float() etc..)
	-> __name__, __hash__, __init__, etc comes from 'object' class.. [dir(object) will give you the list.]

We can override methods from any parent class in any of the children class.
	-> class A:
		class B(A):
			class C(B)

	Class C can override methods from class A, even if class B has not defined then in its definition.

Objects have property: __class__	-> return 'class' the object was created from		-> (type() does the same thing)
Classes have property: __name__		-> return 'string' containing the name of the class
	-> To get name('string') of the class an object is created from
		-> object.__class__.__name__

Extending: Adding features in Child-class that are not in the parent class.
			-> Basically, anything in child-class that is not overriding stuff from parent-class is extending the child-class.

Just FYI:
	-> Any Parent-Class that implements certain functionality which is incomplete, and need the Child-Class to complete them before using them.
		Such Parent-Class are called as 'Abstract Classes'.
		Eg:
			Class Person:
				def routine(self):
					uses 3 methods

				..2 methods are in parent class./

			Child class need to implement the remaining 'method' before using routine()..
			Person call is an Abstract Class.
'''

print('------------------------------------- Inheritance and Overriding -------------------------------------\n')

class Person:
	def __init__(self, name):
		self.name = name

	def __repr__(self):
		return f"\tCool Stuff -> '{self.__class__.__name__}' <-\t\t(name={self.name})"

	def eat(self):
		return 'Person Eat'

	def work(self):
		return 'Person Work'

	def sleep(self):
		return 'Person Sleep'

	def routine(self):
		print(self.eat())
		print(self.work())
		print(self.sleep())

class Student(Person):
	def work(self):
		return 'Student Studies'

p = Person('Alex')
s = Student('Peter')

print('Instance of Person:', p)
print('Instance of Student:', s)

#######################################################
# Even if routine() is defined in Person, when we call s.routine(), self.work() will get overriden.
# For any function call, even when calling the inherted function, any dependent function implementation is checked from child-to-parent..
# this is because of 'self'.. 'self' is always bound to the instance of the class an attribute / function is called from.
#######################################################

s.routine()

print('\n\n------------------------------------- Using Class Attributes to Undermine Instance Values -------------------------------------\n')

class Account:
	apr = 3.0

	def __init__(self, account_number, balance):
		self.account_number = account_number
		self.balance = balance
		self.account_type = 'Generic Account'

	# self.__class__ == type(self)
	def calc_interest(self):
		return f'Calc Interest on {self.account_type} with APR = {self.__class__.apr}'

class Saving(Account):
	apr = 5.0

	def __init__(self, account_number, balance):
		self.account_number = account_number
		self.balance = balance
		self.account_type = 'Generic Account'

# Now, in any instance, if APR is given anything.. Calc_interest() will still use the hardcoded 'apr' value from class
s = Saving(134, 23)
s.apr = 10.0
print('Calc Interest for Savings: ', s.calc_interest())