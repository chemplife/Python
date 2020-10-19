'''
CHAINING:
	itertools.chain(*args)				-> all 'args' should be ITERABLES/ITERATORS
										-> LAZY ITERATOR
	
	If arg is an iterator/iterable of iterables, this will unpack EAGERLY.
	To keep the unpacking LAZY there is another method

	itertools.chain.from_iterables(l)	-> l is the iterable if iterables
										-> LAZY ITERATOR

TEE:
Copy iterator, to go over an iterator multiple times or even parallel
	tee(iterable, times)				-> returns tuple of length 'times': (iter1, iter2,...., iter10)
										-> all the copies are independent of each other.
										-> all copies are LAZY ITERATORS, even if original was ITERABLE
'''