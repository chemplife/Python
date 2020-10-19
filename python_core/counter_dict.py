print('--------------------- Regular Count ---------------------\n')
d={}
for i in range(5):
	d['key'] = d.get('key', 0) + 1
print('Counter Dict 1:', d)

print('\n\n--------------------- Defaultdict Count ---------------------\n')

from collections import defaultdict, Counter

d = defaultdict(int)
for i in range(5):
	d['key'] += 1
print('Counter Dict 2:', d)


print('\n\n--------------------- Counter ---------------------\n')
'''
counter: Dict type that can have repeated 'Keys'
	-> acts like defaultdict with default value = 0
	-> Supports same constructors as regular dicts
	-> autocalculate frequency table based on any iterable
	-> find 'n' most common items
	-> increment / decrement counters based on other Counters or Dicts or Iterables

** fromkeys() not supported
** update works Differently than regular dict.
	-> it does in-place addition of counts. (if we add any item that is already there in the counter_dict,
		it will just increment the count of that item by 1)
** iterable is just a sequence of elements and not a Tuple
'''

counter = Counter()
for i in range(5):
	counter['key'] += 1

print('Counter Dict 3:', counter)

# with value in Counter()

c1 = Counter('able was I ere I saw elba')
print('With value count: ', c1)

print('Most common 3:', c1.most_common(3))
print('Each element of the Counter Dict:\n', list(c1.elements()))

print('\n---------------- Regular Dict Functionality ----------------\n')
c2 = Counter(a=20, b=30)
c3 = Counter({'a': 50, 'b':40})
print(f'Counter Regular Dict 1: {c2}\nCounter Regular Dict 2: {c3}')


# How to Implement elements() functionality in Regular Dictionary

class RepeatIterable:
	def __init__(self, **kwargs):
		self.d = kwargs

	def __setitem__(self, key, value):
		self.d[key] = value

	def __getitem__(self, key):
		self.d[key] = self.d.get(key, 0)
		return self.d[key]

	def elements(self):
		for k, freq in self.d.items():
			for _ in range(freq):
				yield k

r = RepeatIterable(a=10, b=5)
print('New value: ', r['x'])
print('R dict: ', r.d)
print('Elements: ', list(r.elements()))

print('\n\n---------------- Update Counter with other Counter / Dict / Iterable ----------------\n')

c4 = Counter(a=1, b=2, c=3)
c5 = Counter(b=3, c=4, d=5)
c4.update(c5)
print('Updated counter c4 For Addition: ', c4)

c4.subtract(c5)
print('Updated counter c4 For Subtraction: ', c4)

c4.update('aaabbccccccdddeee')
print('Updated counter c4 For Iterable: ', c4)

# update() and subtract() mutates the Counter() Object
# c4 + c5 AND c4 - c5 will create new Counter() Object

print('Get Minumum: ', c4&c5)
print('Get Maximum:', c4|c5)

c6 = Counter(a=10, b=-2, c=0)

# This will create a new object
print('Get only +ve counter value: ',+c6)
print('Get only -ve counter value: ',-c6)


from itertools import repeat

print('Repeat: ', list(repeat('a', c6['a'])))
t = ('a', 2)
print('Repeat tuple: ', list(repeat(*t)))


from itertools import chain
# Chain takes a callable as argument which gives out multiple iterables and create 1 iterable.
print('Chain the iterables: ', list(chain.from_iterable(repeat('b', c5['b']) for _ in range(5))))