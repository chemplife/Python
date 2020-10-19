'''
Given:
	1,2,3,4,5,6,7,8..
	N, S, E, W

Output:
	1N, 2S, 3E, 4W, 5N, 6S, 7E, 8W..
'''

# Cyclic Iterator: This is infinite
# To make it finite, uncomment the length section and pass in the length during object creation
class CyclicIterator:
	def __init__(self, lst, length=0):
		self.list = lst
		self.i = 0
		self.length = length

	def __iter__(self):
		return self

	def __next__(self):
		# if self.i >= self.length:
		# 	raise StopIteration
		# else:
		result = self.list[self.i % len(self.list)]
		self.i += 1
		return result

iter_cycle = CyclicIterator('nswe')
n = 11
seq_1 = [str(i) + str(next(iter_cycle)) for i in range(1,n+1)]
print(f'sequence: {seq_1}')
seq_2 = [str(i) + str(next(iter_cycle)) for i in range(1,n+1)]
print(f'sequence: {seq_2}')



# Problem 1: Currently, the 2nd sequence is picking up the directions, where sequence_1 left off.
# Problem 2: Can there be a simpler approach?

import math

directions = 'NSWE'
ce = math.ceil(n/4)
seq = [f'{val}{direction}' for val, direction in zip(range(1,n+1), directions*ce)]
print('Final Seq:', seq)

# Way 2:
import itertools
iter_cycle = itertools.cycle('NSWE')
seq_it = [f'{i}{next(iter_cycle)}' for i in range(1,n+1)]
print('Itertools seq:', seq_it)


'''
If a class object parameter is an iterable, we don't need to define an iterator inside the __iter__ method of that class.
This is called Deligating Iterables.
eg:
'''
print('---------------------------------------------------------------------------------------------------')
from collections import namedtuple

Person = namedtuple('Person', 'first last')
person = [Person('mike', 'tySon'), Person('eriC', 'bAna'), Person('pAul', 'ruD'), Person('Tony', 'STark')]

class PersonName:
	def __init__(self, persons):
		try:
			self._persons = [person.first.capitalize()+' '+person.last.capitalize() for person in persons]
		except (TypeError, AttributeError):
			self._persons = []

	def __iter__(self):
		return iter(self._persons)

person_names = PersonName(person)
#Now, person_names is iterable itself
for name in person_names:
	print(name)