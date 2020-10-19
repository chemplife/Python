'''
Grouping iterators based on the first element of the iterable.
Eg: [1,10,100]			-|
	[1,1000,2000]		 |	Group 1
	[1,4000,6000]		-|
	[2,20,200]			-|	
	[2,500,5000]		-|	Group 2
	[3,30,300]			-|
	[3,3000,7000]		 |	Group 3
	[3,3500,9000]		-|

itertools.groupby(iterable, [keyfunc])
	-> Returns LAZY ITERATOR
	-> default keyfunc is iter[0]
	-> return values will be TUPLES

*** NEED SORTED ITERABLE before grouping
'''
from itertools import groupby

l = (1,1,1,2,2,3,3,3)
g_l = groupby(l)
#print('Grouping:\n',list(g_l))
print('Values:\n', [(key, list(val)) for key, val in g_l])


#If not sorted
l_1 = (1,1,1,2,2,3,3,3, 1)
g_l_1 = groupby(l_1)
#print('Grouping unsorted:\n',list(g_l_1))
print('Values unsorted:\n', [(key, list(val)) for key, val in g_l_1])

l_l = [[1,10,100], [1,1000,2000], [1,4000,6000], [2,20,200], [2,500,5000], [3,30,300], [3,3000,7000], [3,3500,9000]]
g_l_l = groupby(l_l, lambda x: x[0])
print('Values List of Lists:\n', [(key, list(val)) for key, val in g_l_l])