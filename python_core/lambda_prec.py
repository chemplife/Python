'''
lambda needs to be a single expression function.
'''
def apply_func(fn, *args, **kwargs):
	print(kwargs)
	print(args)
	return fn(*args, **kwargs)

print(apply_func(lambda x,*,y:x+y, 1, y=3))
#Sum() doesn't accept *args. Sum() requires 1 iterable (not dictionary)
print(apply_func(sum, (1,2,3,4,5)))

print('-------------------------------')
print('Sorted function')

l = [1,4,2,8,5,7,3]
m = ['D','a','B','c']
''' help(sorted) -> sorted(iterable(any), Key=function which apply on each element and sorting happens on the basis of result) '''

print('Sorted List:',sorted(l))
print('Original list:',l)

print('Sorted with function:', sorted(m, key=lambda s:s.upper()))
print('Original list:', m)

print('-------------------------------')
print('Randomize list using sort')

import random
print('Randomize l:', sorted(l, key=lambda x: random.random()))