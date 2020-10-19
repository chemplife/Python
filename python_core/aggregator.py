'''
A Function that returns a single value after taking into account every value of an iterable/iterator sequence.
Eg of Aggregators: max(), min() etc.

PREDICATE: Function that takes a single argument and returns TRUE/FALSE.
Eg: bool(), any(), all(), isinstance()

Every element in Python is an object.
Every object has a Truth Value associated to it.
DEFAULT TRUTH VALUE of an object is TRUE, unless certain things happen (Like: None, Empty sequence, 0, etc)
	-> A Class object will looks of '__bool__' or '__len__' to return Truth Value.
	-> If both these methods are not there, DEFAULT is TRUE.
'''

# map(fn, iterable) -> applies 1 function to every element of an iterable
pred = lambda x: x < 10
l = [1,2,3,4,5,10,100]
print(f'Map predicate on list for less than 10.\nList: {l}\nAll Less than 10: {all(map(pred,l))}')
# we can use comprehension as well
print('Using Generator Expression:', (pred(l) for item in l))

print('\n-------------------------------- Generator Default --------------------------------')
def square(num):
	for i in range(num):
		yield i**2

sq = square(5)
print('maximum of squared list:', max(sq))

# This is empty because 'sq' is exhausted
# print('minimum of squared list:', min(sq))

print('Truth value of exhaused generator: ', bool(sq))
''' Truth value of exhaused generator is TRUE.
-> Because it is a generator type and it's default value is true unless we specify it to be false.
-> Make a custom class for that
	eg:
		class Gen:
			def __bool__(self):
				return False
	OR
		class Gen:
			def __len__(self):
				return 0
'''

print('\nAny() example: ',any([0,0,0,0,0,0,0,1]))

#Length is not zero.
print('Truth value of List with 0 as element: ', bool([0]))
