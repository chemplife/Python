'''
UserDict (from collections)

- It is not technically a subclass of 'Dict'
- It uses a regular dictionary as a backing data structure and implements key functionalities of 'Dict'
- It is written in 'Python' so, any Method we override, even 'parent-class' object will use it. It won't go to C level.
	-> .get(), .update(), .len() all are Built-in type C functions
		-> when called, they go to C for operation. Therefore cannot be overriden

- It is not a 'Dict', it is a 'Mapping_Type'
'''

print('------------------------- Custom Dictionary -------------------------\n')
# Store Value for a Key only if it is Real and on getitem give truncated value out

from numbers import Real

class IntDict:
	def __init__(self):
		self._d = {}

	def __setitem__(self, key, value):
		if not isinstance(value, Real):
			raise ValueError('Value Needs to be a Real Number')
		self._d[key] = value

	def __getitem__(self, key):
		return int(self._d[key])


d = IntDict()
d['a'] = 10.5
print('Dict: ', d)
print('Value of a:', d['a'])

# This won't work as this method does not exist
#print("Value of 'a' with get(): ",d.get('a'))

#And for not-Real-Number Values, we will get an error.
# but we lost a lot of functionality of Dictionary Objects, like update(), get(), etc.

#Inheriting IntDict from 'dict' will give us access to those functionalities.
print('\n\n-------------------- Trying Inheritance to fix lost-functionality issue --------------------\n')
class IntDict_2(dict):
	def __setitem__(self, key, value):
		if not isinstance(value, Real):
			raise ValueError('Value Needs to be a Real Number')
		
		super().__setitem__(key, value)

	def __getitem__(self, key):
		return int(super().__getitem__(key))

d = IntDict_2()
d['a'] = 10.5
print('Dict: ', d)
print('Value of a:', d['a'])
#.get() will return 10.5 for d['a'] because it does not use our __getitem__() method
print('Value of key with get(): ', d.get('a'))

# Dict functions that we can use now.
print('\nKeys: ', d.keys())

# Interesting STUFF
d.update({'d': 'python'})
print('\nDict after update: ', d)

##### This will give error
#print("Value of key 'd': ", d['d'])
##### This will work though
print("Value of key 'd': ", d.get('d'))

d1 = {}
d1.update(d)
print('D1 Dict: ', d)


print('\n\n---------------------------------------- Using UserDict ----------------------------------------\n')

from collections import UserDict

class IntDict_3(UserDict):
	def __setitem__(self, key, value):
		if not isinstance(value, Real):
			raise ValueError('Value Needs to be a Real Number')
		
		super().__setitem__(key, value)

	def __getitem__(self, key):
		return int(super().__getitem__(key))

d = IntDict_3()
d['a'] = 10.5
d['b'] = 100.5

# This will give error from IntDict_3 class
#d['c'] = 'python'

print('Dict: ', d)
print('Value of a:', d['a'])
print('Value of key with get(): ', d.get('a'))

# This willnot throw an error fron IntDict_3 class
#d.update({'d': 'python'})

d1 = {}
d1.update(d)
print('\nD1 Dict: ', d1)

print('\nActual D data: ', d.data)
print(f"Type of dict 'd'= {type(d)}\n\tAnd 'd.data'= {type(d.data)}")


print('\n\n---------------------------------------- UseCase of Child-Only-Mutable-Feature ----------------------------------------\n')
# We want to create a dict that has Keys only in Reb, Green, Blue and Values from 0-255

class LimitedDict(UserDict):
	def __init__(self, keyset, min_val, max_val, *arg, **kwargs):
		self._keyset = keyset
		self._min_val = min_val
		self._max_val = max_val
		super().__init__(*arg, **kwargs)

	def __setitem__(self, key, value):
		if key not in self._keyset:
			raise KeyError(f"Invalid Key name. Has to be from set:{self._keyset}")

		if not isinstance(value, int):
			raise ValueError('Value Needs to be an integer.')

		if value < self._min_val or value > self._max_val:
			raise ValueError(f'Value Needs in range {self._min_val} - {self._max_val}.')

		super().__setitem__(key, value)


keyset = ('red', 'green', 'blue')
d = LimitedDict(keyset, 0, 255, red=10, green=10, blue=10)

d['red'] = 100
d['green'] = 50
d['blue'] = 150

# d['purple'] = 10	-> will throw error
# d['red'] = 50		-> will throw error
# d['green'] = 1.23	-> will throw error

print('Color Dict: ', d)


#Interestingly, below one will throw error, even though we are sending those values to 'super() class'.
# This is because after overiding a parent class method in child class,
# any operation called on overriden parent class method will be redirected towards that function's implementation in Child class

#d1 = LimitedDict(keyset, 0, 255, red=10, green=1000, yellow=10)