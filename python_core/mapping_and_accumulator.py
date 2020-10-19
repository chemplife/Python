'''
map(fn, iterable): applying a callable to each element of the iterable
				-> returns LAZY ITERATOR

accumulator: reducing an iterable to a single value.
	Eg: sum(), max(), min(), reduce(fn, iterator, [initializer])
'''
import functools, operator

print('-------------------------------- Reduce --------------------------------')
# fn always takes 2 arguments
l = [1,2,3,4,5,6,7]
r = functools.reduce(lambda x,y: x+y, l)
print('Reduced:', list(r))


print('\n-------------------------------- Starmap --------------------------------')
import itertools

# It unpacks the subelements of the iterable into arguments.
# returns LAZY ITERATOR
l_nested = [[1,2],[3,4]]
print('Map:', list(map(lambda item: item[0]*item[1], l_nested)))
print('Generator:', list(operator.mul(*item) for item in l_nested))
print('Starmap:', list(itertools.starmap(operator.mul, l_nested)))


print('\n-------------------------------- Accululator --------------------------------')
# Similar to reduce()
# But returns all the intermediate values as well.
# accumulate(iterable, [fn]): Default is Add.
# Returns a LAZY ITERATOR

print('Accululator on list l:', list(itertools.accumulate(l,operator.mul)))
