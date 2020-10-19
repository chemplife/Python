# Anything that can have (), like a function is a callable.
# A callable ALWAYS returns a value.
print(callable(print))

#make object of a class callable
class MyClass_1:
	def __init__(self, x=0):
		print('Initializing Class 1...')
		self.counter = x

class MyClass_2:
	def __init__(self, x=0):
		print('Initializing Class 2...')
		self.counter = x

	def __call__(self, x=1):
		print('Updating Counter...')
		self.counter+=x

a = MyClass_1(100)
b = MyClass_2(100)
print('callable Class 1 Object:',callable(a))
print('callable Class 2 Object:',callable(b))
b()
print('class 2 object counter:',b.counter)