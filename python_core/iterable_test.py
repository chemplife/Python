t = (1,2,3,4)
l = [1,2,3,4]
s = {1,2,3,4}
d = {'a':1, 'b':2, 'c':3, 'd':4}
st = 'abce'

# set and dictionary -> s[0], d[0] WON'T WORK. They are UNORDERED.

# UNPACKING
# 1. Tuple
a,b,c,e = t
print(f'Tuple: a={a}, b={b}, c={c}, e={e}')

# 2. List
a,b,c,e = l
print(f'List: a={a}, b={b}, c={c}, e={e}')

# 3. String
a,b,c,e = st
print(f'List: a={a}, b={b}, c={c}, e={e}')

# 4. Set
# May get different sequence for a,b,c,e. Same for dictionary
a,b,c,e = s
print(f'Set Run1: a={a}, b={b}, c={c}, e={e}')
print(f'Set Run2: a={a}, b={b}, c={c}, e={e}')

# Same. different sequence. Search by element works best, and is freaky fast.
for e in s:
	print('Set iteration:',e)

# 5. Dictionary
# gives keys
for a in d:
	print('Dictionary Keys:',a)

# gives values
for a in d.values():
	print('Dictionary Values:',a)

# gives both
for a,b in d.items():
	print(f'Key:{a}, Value:{b}')

# Put first element in a and rest as LIST in b. Works for ALL ITERABLES
a,*b = t
print(f'Tuple New: a={a}, b={b}')

a,*b = l
print(f'List New: a={a}, b={b}')

a,*b = st
print(f'String New: a={a}, b={b}')

a,*b = s
print(f'Set New: a={a}, b={b}')

a,*b = d
print(f'Dictionary New: a={a}, b={b}')

# Works like this too. But ONLY 1 with '*'
# a = 1st , b = 2nd , d = Last, c = rest
a,b,*c,e = (1,2,3,4,5,6,7,8)
print(f'Tuple Diff: a={a}, b={b}, c={c}, e={e}')

# We can MERGE Iterables as well
m = [*t, *l, *st, *s, *d]
print(f'Merged as List: {m}')

# Merge as Set (UNORDERED Iterable), will remove repeated elements.
# Set don't have repeated elements.
m = {*t, *l, *st, *s, *d}
print(f'Merged as Set: {m}')

# DICTIONARY Special Case
'''
	Unpack Key-Value Pair.
	'**' only for LHS
	If Key repeats, the last unpacked Dictionary Value OVERRIDES the previous value
		- d3.h = 4 will get overriden by d3.h = 1
'''
d2 = {'e':1, 'f':2, 'g':3, 'h':4}
d3 = {'h':1, 'i':2, 'j':3, 'k':4}
m = {**d, **d2, **d3}
print(f'Dictionary Special Case_1: {m}')

d4 = {'a':10, 'j':2, **d}
d5 = {**d, 'a':10, 'j':2}
print(f'Dictionary Special Case_2: {d4}')
print(f'Dictionary Special Case_3: {d5}')

# Nested Unpacking: ONLY TO ORDERED Iterables
# Multiple '*' are allowed if they are nested 
a,*b,(e,f,g),(h,*i,[k,o,(m,n)]) = [1,2,3,'XYZ', (5,6,7,{8,9,'AB'})]
print(f'Nested Unpacking: a={a}, b={b}, e={e}, f={f}, g={g}, h={h}, i={i}\
, k={k}, o={o}, m={m}, n={n}')

# Union is same as unpacking for SETs
# Unpack as List will retain repeated elements.
# We don't have to create a new variable for any of these.
s2 = {1,2,3,4,5,6,7}
s3 = {7,8,9}
s_union = s.union(s2,s3)
s_unpack = {*s,*s2,*s3}
s_unpack_list = [*s,*s2,*s3]
print(f'Set Union: {s_union}')
print(f'Set Unpack: {s_unpack}')
print(f'Set Unpack in List: {s_unpack_list}')

# Unpack Unknown length for any ORDERED Iterable
# z[-1] = Last element
# z[1:] = 2nd element onwards
z = [1,2,3,4, 'python']
a,b,c,e = z[0],z[1:-1],z[-1][0],list(z[-1][1:])
print(f'Unknown Length List Unpack: a={a}, b={b}, c={c}, e={e}')


print('''\n\n########################################################################################################################
######################################################### Part 2 #######################################################
########################################################################################################################\n''')

# Careful about string concatination
# nesting IMMUTABLE sequence multiplication generates a new sequence
list_1 = [1,2]
list_1_2 = list_1*2
print(f'Address of:\n\tlist_1= {id(list_1)}\n\tlist_1_2= {id(list_1_2)}')

# But nesting MUTABLE sequence in essense refers to the same address in memory.
# So, if 1 position is changed, change is reflected in other part of the list too.
nest_list_1 = [[1,0]]
nest_list_1_2 = nest_list_1*2
print(f'Address of:\n\tnest_list_1= {id(nest_list_1[0])}\n\tnest_list_1_2= {id(nest_list_1_2[1])}')
nest_list_1[0][0] = 100
print(f'New nest_list_1= {nest_list_1}\nNew nest_list_1_2= {nest_list_1_2}')


# Iterable: Sequence that we can iterate through
# Sequence: Sequence that supports indexing.

print('------------------------- Slice -------------------------')

'''
Slicing: slice is an object (like everything else in Python) of type: slice
		For k > 0
		- if 'i' or 'j' > len(sequence) -> len(sequence) 					===== NO exception.
		- if 'i' or 'j' < 0 			-> max(0, len(sequence)+ i or j) 	===== NO exception.

		For k < 0
		- if 'i' or 'j' > len(sequence) -> len(sequence) -1 				===== NO exception.
		- if 'i' or 'j' < 0 			-> max(-1, len(sequence)+ i or j) 	===== NO exception.

# ****** ALWAYS creates a NEW object ******
'''

a = [1,2,3,4,5,6,7,8,9]
s = slice(0,2)
print(f'List a: {a}')
print(f'Slice of a with [i:j) notation: {a[0:2]}')
print(f'Slice of a with slice(i,j) notation: {a[s]}')

print(f'start of slice: {s.start}')
print(f'stop of slice: {s.stop}')
# default step is 1/None
print(f'step of slice: {s.step}')

print(f'selection with stride [i,j,k]: {a[2:500:3]}')

print(f'selection with reverse stride [i,j,-k]: {a[len(a):-400:-2]}')

# To get the exact START, STOP, STEP for a sequence.
# -> slice(start, stop, step).indices(seq_len) = (start, stop, step)
print(f"Exact indices for slicing for list 'a' for positive step: {slice(0,20,1).indices(len(a))}")
print(f"Exact indices for slicing for list 'a' for negitive step: {slice(10,-20,-1).indices(len(a))}")
# list -> range -> unpack slice tuple
print(f"Create a list from slice.indices: {list(range(*slice(10,-20,-2).indices(len(a))))}")


print('------------------------- Mutation by slice -------------------------')
l = [1,2,3,4]
print(f'List l: {l}')
print(f'Address of l: {id(l)}')

# Replacement iterable size doesn't matter
l[1:3] = (5,6,7,8)
print(f'List l after replacement: {l}')
print(f'Address of l: {id(l)}')

# this will return 2 elements, so we must provide the EXACT EQUAL length of iterable for replacement.
l[0:3:2] = [10, 20]
print(f'List l after step-replacement: {l}')
print(f'Address of l: {id(l)}')

l[1:3] = []
print(f'List l after deletion: {l}')
print(f'Address of l: {id(l)}')

l[1:1] = ('abc')
print(f'List l after insertion at index 1: {l}')
print(f'Address of l: {id(l)}')


print('------------------------- In-place concatination / Mutation -------------------------')

l1 = [1,2,3,4]
l2 = [5,6,7,8]

t1 = (1,2,3,4)
t2 = (5,6,7,8)

# l1 = l1+l2 		!=		l1 += l2
# Same thing happens for repetition
# l1 = l1 * 2 		!=		l1 *= 2
print(f'Address of L1: {id(l1)}')
l1 = l1+l2 
print(f'l1 = l1 + l2 will create a new list: {id(l1)}')

l1 = [1,2,3,4]
print(f'Address of L1: {id(l1)}')
l1 += l2
print(f'l1 += l2 will mutate l1: {id(l1)}')

l1 = [1,2,3,4]
print(f'Address of L1: {id(l1)}')
l1 += t1
print(f'we Can even do l1 += t1: {id(l1)}')
print('\nl1 = l1 + t1 \nwill give error that list cannot concatinate with tuple.\
	\nBut you can mutate list with tuple. Any sequence works for mutation\n')


# For Tuples: since they are not mutable
# t1 = t1+t2 		==		t1 += t2
# Same thing happens for repetition
# t1 = t1 * 2 		==		t1 *= 2
print(f'Address of T1: {id(t1)}')
t1 = t1+t2 
print(f't1 = t1 + t2 will create a new tuple: {id(t1)}')

t1 = (1,2,3,4)
print(f'Address of T1: {id(t1)}')
t1 += t2
print(f't1 += t2 will also create a new tuple: {id(t1)}')


'''
To create custom iterator:

Need to implement iterator protocol.
	- __iter__: 	returns a new instance of iterator object to iterate over the iterable.
	- __next__:		returns next object in the iterator, and need to have 'raise StopIteration' when iterator length is reached.

'''

# without __iter__, python doesn't know that we are implementing 'iterator protocol'.
# currently, 'for loop' will go into infinite loop because it doesn't know when to stop
# we can use 'while' to see the result
class Squares:
	def __init__(self, length):
		self.i = 0
		self.length = length

	def __next__(self):
		if self.i >= self.length:
			raise StopIteration
		else:
			result = self.i ** 2
			self.i += 1
			return result

sq = Squares(5)

while True:
	try:
		print(next(sq))
	except StopIteration:
		print('End of length')
		break


# with __iter__, for loop know that the 'sq' object is an iterable
class Squares_2:
	def __init__(self, length):
		self.i = 0
		self.length = length

	def __next__(self):
		if self.i >= self.length:
			raise StopIteration
		else:
			result = self.i ** 2
			self.i += 1
			return result

	def __iter__(self):
		return self

sq = Squares_2(5)
for item in sq:
	print(item)

'''
Iterable: Created once: collection of object that can be iterated upon.
		(__iter__: returns new iterator instance to iterate over the iterable)

Iterator: Created everytime we need to iterate over an iterable: Becomes throwaway object after use.
		(__iter__: returns itself, an iterator. Not a new instance)
		(__next__: returns the next element)

Sequence: It is an iterable without __iter__
		(__getitem__: returns a new iterator instance that raises StopIteration error when iterator is exhausted)
		(if NO StopIteration exception: it will return TypeError stating that the sequence is not iteratable.)

iter(obj): Looks for __iter__ first, then __getitem__

Eg: You can iterate over sq only once because it is an ITERATOR, not an ITERABLE
Next time we need to create the object again
'''
# this will not print anything as sq is now empty.
for item in sq:
	print(item)