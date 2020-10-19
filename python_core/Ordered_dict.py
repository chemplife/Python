'''
Python3.6 onwards, Dictionary are going to be ordered by default.
'OrderedDict' is mainly used for Backward Compatibility of programs.

Unique Features:
	-> Supports Reverse Iterations of Keys
	-> Pop 1st and last items of Dictionary
	-> Move Items to the Beginning or End of Dictionary

For Python 3.6 and up,
Dict is already retaining the order of Keys since the assignment.
Features Present:
	-> Pop Last item
'''

from collections import OrderedDict

# d = OrderedDict(a=2, b=2) -> Not recommended because the argument sequence is not guaranteed before Python 3.5
d = OrderedDict()
d['a'] = 1
d['b'] = 2
d['c'] = 3
d['d'] = 4
d['e'] = 5

print('Dict: ', d)
print('\nReversed Dict: ', list(reversed(d)))
print('\nPop item: ', d.popitem(), "\n", 'Dict now: ', d)
print('\nPop 1st item: ', d.popitem(last=False), "\n", 'Dict now: ', d)
print('\nMove to end: ', d.move_to_end('b'), "\n", 'Dict now: ', d)
print('\nMove to front: ', d.move_to_end('d', last=False), "\n", 'Dict now: ', d)