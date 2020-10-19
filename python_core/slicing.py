'''
How to Slice Iterables in general (Not just sequence type)
itertools.islice

Sequence:	-> s[i:j:k]
			-> seq[slice(i,j,k)]

Iterable:	-> islice(iterable, start, stop, step)
		: It will iterate over the iterable and find out which slice to YIELD back.
		: islice -> Returns a LAZY ITERATOR.
'''

##
# ****** We will use 'YIELD' in iterable_generating_function. So, it will not calculated unrequired values.. ******
##

#Custom Slicer function
print('------------------------------ Custom Slicer ------------------------------')
from math import factorial

def slice_(iterabl, start, stop):
	for _ in range(0, start):
		next(iterabl)
	for _ in range(start, stop):
		yield next(iterabl)

def facto(num):
	for i in range(num):
		print(f'Yielding factorial of {i}')
		yield factorial(i)

print('Slice 0 - 6:', list(slice_(facto(10), 0, 6)))
print('Slice 3 - 6:', list(slice_(facto(10), 3, 6)))

print('\n------------------------------ Using islice ------------------------------')

from itertools import islice

print('Slice 0 - 6:', list(islice(facto(10), 0, 6)))
print('Slice 3 - 6:', list(islice(facto(10), 3, 6)))

#islice returns a Lazy iterator. So, it won't execute the function in it, until we request values.
print(f'{islice(facto(10),3,6)}\t<-\tInside function not executed. Just an iterator is commissioned')

fc = islice(facto(10),0,9)
print('Printing few for the islice(): ', next(fc), next(fc), next(fc))

# ****** ISLICE -> returns LAZY ITERATOR. It will exhaust the used values.
print('Printing islice full: ', list(fc))