'''
itertools.product(*arg)		-> will gives the Cartesian Product of the arguments.
							-> [1,2],[3,4] = [1,3],[1,4],[2,3], [2,4]
							-> and grows exponentially depending on the number of args
							-> Returns LAZY ITERATOR

itertools.permutations(iterable, r=None)
							-> Elements of iterable are consider UNIQUE based on their POSITION, not VALUE.
									->So, DON'T Sort the results.
								-> If iterable has repeat values, then permutation will also have repeat values.
							-> r = Size of the permutation.
							-> r = None : each permutation is the size of iterable.

itertools.combinations(iterable, r=None)
							-> Order of elements are not considered (unlike permutation)
								-> So, it is OK to sort the combinations result.

							-> (without replacement option) itertools.combinations()
								-> we cannot pick an element from the iterable while operating if the element is picked before
								-> Similar to what happens in ITERATORS

							-> (with replacement option) itertools.combinations_with_replacement()
								-> you can pick the element from the set again.
								-> Similar to ITERABLES
'''

import itertools

print('-------------------------------- Cartesian Product --------------------------------')
l1 = ['x1', 'x2', 'x3', 'x4']
l2 = ['y1', 'y2', 'y3']
print('Regular For Loop:')
for x in l1:
	for y in l2:
		print(f'({x},{y})', end='\t')
	print('\n')

print('\nUsing Itertools.product')
print(list(itertools.product(l1,l2)))

print('\n---- Matrix ----')
def matrix(n):
	yield from itertools.product(range(1,n+1), range(1,n+1))

# So, product() yields tuple.
print(list(matrix(4)))

# Print product
print('\n---- Matrix Product ----')
def matrix_mult(n):
	for x,y in itertools.product(range(1,n+1), range(1,n+1)):
		yield (x,y,x*y)
print(list(matrix(4)))

# We can go with generators too.
print('\n---- Matrix Product with generators ----')
def matrix_mult_gen(n):
	return((x,y,x*y)
			for x,y in itertools.product(range(1,n+1), range(1,n+1))
		)
print(list(matrix_mult_gen(4)))

# If we have multiple lists.
# we can use 'tee' to make multiple copies
# but we need to unpack iterator 'tee' returns
print('\n---- Matrix Product with generators ----')
def matrix_mult_gen(n):
	return((x,y,x*y)
			for x,y in itertools.product(*itertools.tee(range(1,n+1),2))
		)
print(list(matrix_mult_gen(4)))


print('\n---- Create a Grid for x,y coordinates ----')

from fractions import Fraction
# we can use the same function to create 3-4-5 ant dimension grid.
def grid(min_val, max_val, step, * , num_dimensions = 2):
	# Count will take non-integer steps and we calculate that until we reach the max_val
	axis = itertools.takewhile(lambda x: x<=max_val,
								itertools.count(min_val, step))

	# We calculate the 'axis' for all the dimensions. Default is 2. They need to be independent of each other.
	axes = itertools.tee(axis, num_dimensions)

	# To make the grid, we need the cartesian product of the points.
	# 'Tee' returns an iterable so for product(), we need to unpack it
	return itertools.product(*axes)

print(list(grid(-1,1,0.5)))

print('\n---- Probability of rolling a total of 8 (using cartesian) ----')

sample_space = list(itertools.product(range(1,7), range(1,7)))
print('Sample Space: ', sample_space)

# Find tuples with total of 8
outcome = list(filter(lambda x: x[0]+x[1]==8, sample_space))
print('Outcome: ', outcome)

print('Probability:', Fraction(len(outcome),len(sample_space)))


print('\n\n\n-------------------------------- Permutation and Combination --------------------------------')

from collections import namedtuple

print('Combinations without replacement:',\
		list(itertools.combinations([1,2,3,4],2)))

# Can be used to calculate the posibility of picking 4 Ace's from a deck of card
print('Combinations with replacement:',\
		list(itertools.combinations_with_replacement([1,2,3,4],2)))

print("\n---- calculate the posibility of picking 4 Ace's from a deck of card ----")

SUITS = 'SHDC'
RANKS = tuple(map(str, range(1,10))) + tuple('JQKA')
deck = [rank+suit for suit in SUITS for rank in RANKS]
print('Deck:\n', deck)

# Deck using product()
deck_p = [rank+suit for rank,suit in itertools.product(RANKS,SUITS)]
print('Deck using cartesian product:\n', deck_p)

# Deck using namedtuple
Card = namedtuple('Card', 'rank suit')
deck_nt = [Card(rank, suit) for rank,suit in itertools.product(RANKS,SUITS)]
print('Deck using Namedtuple:\n', deck_nt)

