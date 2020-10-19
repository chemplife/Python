'''
Set:	-> All elements must be distinct in equality(==) and not only identity('is')
		-> All elements must be hashable

Cardinality of Set() = len(set)

** Sets doesn't have any guaranteed Order while printing it or passing it as an argument.

Methods available for Set() operations (All of these returns a new set, NO MUTATION):

	-> s1.isdisjoint(s2)					:	len(s1 & s2) == 0	-> To check if sets are disjoint
	-> s1.union(s2, ...)					:	s1 | s2 ...			-> Union of sets. (can take more than 1 set in argument)
	-> s1.intersection(s2, ...)				:	s1 & s2 ...			-> Intersection of sets. (can take more than 1 set in argument)
	-> s1.difference(s2, ...)				:	s1 - s2 ...			-> Difference between 2 sets. [s1-s2 != s2-s1]
	-> s1.symmetric_difference(s2)			:	s1 ^ s2 ...			-> Union-intersection of 2 sets.		*** this is also ''XOR''
	-> s1.issubset(s2)						:	s1 <= s2 			-> s1 is subset of s2.		 [len(s1) can be equal to len(s2)]
											:	s1 < s2 			-> s1 is proper subset of s2; if s2 has all s1 elements and more.
	-> s1.issuperset(s2)					:	s1 >= s2 			-> s1 contains all elements of s2 and/or more.
											:	s1 > s2 			-> s1 is proper superset of s2; if s1 has all s2 elements and more.


Set Operations (These will MUTATE the Set..)

	-> s1.update(s2)						:	s1 |= s2 			|
	-> s1.intersections_update(s2)			:	s1 &= s2 			|- All these mutate the set on the left side
	-> s1.difference_update(s2)				:	s1 -= s2 			|- In this case, 's1' will get MUTATED.
	-> s1.symmetric_difference_update(s2)	:	s1 ^= s2 			|		's2'.. needs to be set()

** [s1-s2 != s2-s1]

**	Mathematically written operations: 's2' needs to be set()
	Methods							 : 's2' needs to be an ITERABLE.

ForzenSet: Immutable Set, like Tuple is Immutable List (more or less).
			-> Since FrozenSet is immutable sequence of Hashable values, so it can be used for Keys in dictionary.
			-> Set-of-sets is possible only if the Set containing other Sets is FrozenSet.
			-> Resultant set for | & - ^ will be based on the type of 1st operand.
'''
print('---------------------------- Creating / Modifying Sets ----------------------------')
s1 = {'a', 1, 10.34}						# Linear			|
s2 = set(range(5))							# set(iterable)		|- Must have Hashable Values
s3 = set()									# Empty set -> set()|- in the iterable, linear, and list comprehension
s4 = {c for c in 'python'}					# set Comprehension	|
print(f'Sets:\n{s1}\n{s2}\n{s3}\n{s4}')

print('Combine 2 sets:', {*s1 , *s2})
print(f'Unpack 2 sets in list: {[*s1 , *s2]}')

# Add, remove will mutate set.
print('\nAddress of s1: ', id(s1))
s1.add('b')
print('Address of s1 after adding: ', id(s1))
s1.remove('b')
print('Address of s1 after removing: ', id(s1))

#Removing something that is not in set will give KeyError. Use 'discard' instead
print("\ns1 before discarding 'z': ", s1)
s1.discard('z')
print("s1 after discarding 'z': ", s1)

# Clear will mutate the set and empty it. We still have the set though.
print("\ns1 before clearning: ", s1)
print('Address of s1 before clear: ', id(s1))
s1.clear()
print("s1 after clearning: ", s1)
print('Address of s1 after clear: ', id(s1))
s1.add(('a', 1, 10.34))
print("s1 after adding values: ", s1)
print('Address of s1 after adding values: ', id(s1))