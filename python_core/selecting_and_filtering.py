'''
** For predicate: Read Aggregator.py

FILTER:
filter(predicate ,iterable)
		-> if predicate returns true for any element in the iterable, it is give it out.
		-> returns LAZY ITERATOR
		-> YIELDs the value
		-> you can do the same using: (item for item in iterable if pred(item))
			-> If pred is None, it looks for TRUTH VALUE: (item for item in iterable if item)

itertools.filterfalse(predicate, iterable)
		-> Yields elements that predicate returned FALSE

itertools.compress(i_list, i_selector)
		-> filtering one iterable using TRUTH VALUE of items in another itererable.
		-> LAZY ITERATOR
		-> YIELDs value

itertools.takewhile(predicate, iterable)
		-> YIELDs value till the point pred(element) is TRUE.
			-> The moment pred(element) is FALSE, iterator exhausts
		-> LAZY ITERATOR

(opposite result of 'takewhile')
itertools.dropwhile(predicate, iterable)
		-> YIELDs value after the point pred(element) is FALSE.
			-> Until pred(element) is TRUE, it does not iterate
			-> Basically, pred(element) == FALSE indicate the 'STARTING POINT'. YIELD everything after that.
		-> LAZY ITERATOR
'''

import itertools

#Custom Filter function
print('------------------------------ Custom Filter ------------------------------')

l_1 = [1,2,3,4,5,6,7,8]
print('List: ', l_1)
print('Filtered Elements greater than 4: ',list(filter(lambda x: x > 4,l_1)))

print('\n------------------------------ Compress Filter ------------------------------')

l_2 = ['a', 'b', 'c', 'd', 'e']
selectors = [True, False, 1, 0]

print(f'Using Compress Filter on: {l_2}\nUsing Selector: {selectors}')
# 1 to 1 mapping, like zip: a -> True, b -> False, c -> 1, d -> 0, e -> None
print('Compress Filtered: ', list(itertools.compress(l_2, selectors)))

print('\n------------------------------ Takewhile Filter ------------------------------')

l_3 = [1,3,5,2,0]
print('List: ',l_3)
print('Takewhile for (< 5): ', list(itertools.takewhile(lambda x: x<5, l_3)))

print('\n------------------------------ Dropwhile Filter ------------------------------')

l_4 = [1,3,5,2,0]
print('List: ',l_4)
print('Dropwhile for (< 5): ', list(itertools.dropwhile(lambda x: x<5, l_4)))