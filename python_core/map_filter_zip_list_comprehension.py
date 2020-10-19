##############################################################################
'''
Generators can only be iterated upon ONCE.
We cannot go back and use them again.
Store it into something like, LIST or TUPLE, to use the result multiple times.

Except 'range()' -> it retains the value for future use
'''
##############################################################################

print('Map Function')
'''
map(fn(),*iterables)-> 
	returns: 	generator (iterable). So, convert it into something.
	*iterables: number of iterabels should be equal to arguments taken by fn()
	fn():		operates on all the iterables in parallel, and stops as soon as any of the iterables ends.
'''
l1 = [1,2,3,4]
l2 = [20,30,40,50]

print('Multiply each element by 2:',list(map(lambda x:x*2, l1)))
print('Add corresponding elements of 2 lists:',list(map(lambda x,y:x+y, l1,l2)))

print('\n---------------------------------')
print('Filter Function\n')
'''
filter(fn(),iterables)-> 
	returns: 	generator (iterable). So, convert it into something.
	iterables: 	single iterable
	fn():		operates on ONE iterable and checks if value of opration on each element is TRUE.
				If TRUE, it will retain the element. If FALSE, it will toss the element out.
	****		if fn() is None, it will see if each element itself is TRUE or not to keep it.
'''
l3 = [0,1,2,3,4]
print('Print Non-zero elements:',list(filter(None, l3)))
print('Print even numbers:',list(filter(lambda x:x%2==0, l3)))

print('\n---------------------------------')
print('Zip Function\n')
'''
zip(*iterables)-> 
	returns: 	iterable with each corresponding element of iterables put together in a tuple.
				Type is generator (iterable) so, convert it into something.
	*iterables: all the iterables are worked on in parallel, and stops as soon as any of the iterables ends
'''
l4 = 'python'
print('Zip 4 lists:',list(zip(l1,l2,l3,l4)))

print('\n---------------------------------')
print('List Comprehension\n')
'''
[<expression_1> for <element> in <iterable> if <expression_2>]
OR
[<transformation> <iteration> <filter>]

In Words: Iterate over elements of an iterable if expression_2 holds.
		  Calculate expression_1 for those elements and the result will be the element of the new list.

List comprehension in essense is a function within '[ ]'
'''
print('Multiply each element by 2:',[x*2 for x in l1])
print('Add corresponding elements of 2 lists:', [x+y for x,y in zip(l1,l2)])
print('Print even numbers:',[x for x in l3 if x%2==0])

print('\n---------------------------------')
print('Map+Filter v/s List Comprehension\n')
'''
square all the numbers from 0-10, and filter out only those which are small than 25
'''
l = range(10)
seq = list(filter(lambda y: y<25 , map(lambda x: x**2 , l)))
print('map + filter result:	   list(filter(lambda y: y<25 , map(lambda x: x**2 , l))) ->', seq)
seq_lc = [x**2 for x in l if x**2<25]
print('List Comprehension result: [x**2 for x in l if x**2<25] 						  ->', seq_lc)

print('\n---------------------------------')
print('List Comprehension as generator\n')
'''
Map, Filter are better than List Comprehension in a way:
Map and Filter returns generator objects.
	They don't calculate element unless it is needed.

List Comprehension will calcualte element and create a list even if we don't end up using the elements.
'''
# No calculation happens at this step. Only assignment happens
seq_lcg = (x**2 for x in l if x**2<25)
print('List Comprehension as generator:',seq_lcg)

#Now, each element will gets calculated upon request by the loop.
for x in seq_lcg:
	print(x)

#Now, we cannot use it again as it was a generator and only be used ONCE
for x in seq_lcg:
	print(x)


print('''\n\n########################################################################################################################
######################################################### Part 2 #######################################################
########################################################################################################################\n''')

"""
Since List comprehension in essense is a function.

We can create CLOSURES
			  NESTED functions
"""
# num is free variable
def list_comp_closure(num):
	return [i**2 for i in range(num) if i%2==0]

print('''NESTED func:
	[[i*j for j in range(5)] for i in range(10)]
	i is the free variable here
	''')

# we can also have multiple variables iterate till the point used together
# implement zip.

l1 = [1,2,3,4,5,6,7]
l2 = ['a', 'b', 'c', 'd', 'e']
print(f'Zip: {list(zip(l1,l2))}')
l3 = [(item_1, item_2)
		for index_1, item_1 in enumerate(l1)
		for index_2, item_2 in enumerate(l2)
		if index_1 == index_2]
print(f'List_comprehension for zip: {l3}')

print('\n-------------------------------- Zipping Longest --------------------------------')
# Zip_longest(iter1, iter2, iter3, [fillvalue=None]) as per the longest list.
# LAZY ITERATOR RETURNED
import itertools

l5 = [1,2,3,4,5,20,30]
l6 = [5,6,7,8,9]
l7 = [10,11,12]

print('Print as per the longest list: ', list(itertools.zip_longest(l5,l6,l7,fillvalue='N/A')))