'''
The iterators with NO STOP argument.
They all YIELDs value using LAZY ITERATORS
eg:
	itertools.count(start, step)						-> count(10,2): 10,12,14.....
														-> start, stop: Any numeric type (int, float, bool, Decimal, complex)

	itertools.cycle(ITERABLE/ITERATOR/GENERATOR)		-> loop over an ITERABLE/ITERATOR/GENERATOR indefinitely.
	
	itertools.repeat(ITERABLE/ITERATOR/GENERATOR, times)-> Repeats ITERABLE/ITERATOR/GENERATOR specified # of times.
														-> Default is infinite
														-> Object repeated is the same object (they have same Address)
'''
import itertools

print('-------------------------------- Count --------------------------------')
g = itertools.count(1,0.5)
print('Slice of first 5 elements in g for Count: ',list(itertools.islice(g,5)))


print('\n-------------------------------- Cycle --------------------------------')
g = itertools.cycle(('red', 'yellow', 'green'))
print('Slice of first 5 elements in g for Cylce: ',list(itertools.islice(g,5)))

#Look at card_deck_using_yield_and_namedtuple.py file for application.

print('\n-------------------------------- Repeat --------------------------------')
g = itertools.repeat('python')
print('Slice of first 5 elements in g for Repeat: ',list(itertools.islice(g,5)))

g = itertools.repeat('python', 5)
print('Print first 5 elements in g for Repeat with limit: ',list(g))

# Same element problem
g = itertools.repeat([], 4)
g_list = list(g)
g_list[0].append(10)
print('Updated g_list:',g_list)