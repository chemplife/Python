'''
- Standard Dictionary (dict), if we don't find 'key' we get KeyError
- If we use 'd.get(key, defaultValue)'' -> We get either the 'Key' value or the DefaultValue if 'Key' is missing
- But if we have a lot of these 'd.get()' methods that uses a 'Default Value', to maintain consistancy,
	we Need to remember the DefaultValue to put everytime.

DefaultDict- Allow us to define the 'defaultvalue' 1 time and use it everywhere in the program.

defaultdict(callable, [...])
-> Callable: function that will get executed each time a defaultValue is required.
			- Does not take any argument
			- Default is None
			- It can be any function (even an API to get value from DB.)

-> [...] -> remaining arguments are passed to the 'Dict' constructor. These can be
																				- key/value pair, 
																				- keyword Argument
																				- a dictionary to populate new dictionary
																				.. anything we use to populate a dictionary

-> It mutates the Dict if a 'Key' is not found with the default value.
'''

from collections import defaultdict

d = defaultdict(lambda: 'Python')
print("Value of non-existing key d['a']: ", d['a'])
print('Dictionary d: ', d)

print('\n------- Count Example -------\n')
sent_1 = 'elba was I ere I was able'

# Way 1
count_1 = {}
for c in sent_1:
	if c in count_1:
		count_1[c] +=1
	else:
		count_1[c] = 1

# Way 2
count_2 = {}
for c in sent_1:
	count_2[c] = count_2.get(c, 0) + 1

# Way 3
count_3 = defaultdict(lambda:0)
for c in sent_1:
	count_3[c] += 1

print('Count 1: ', count_1)
print('Count 2: ', count_2)
print('Count 3: ', count_3)

print('\n------------ Factory Functions ------------\n')
'''
int(), float(), list(), bool(), str() etc are factory functions that return '0' by default.

-> defaultdict(int) == defaultdict(lambda: 0)
'''
d = defaultdict(int)
print('d[a]: ', d['a'])
print('d: ', d)

print("\n------- 'functools.Partial' Example -------\n")

person = {
	'jack': {'age': 20, 'eye_color': 'blue'},
	'mack': {'age': 25, 'eye_color': 'black'},
	'mike': {'age': 30, 'eye_color': 'brown'},
	'michael': {'age': 35},
	'dean': {'age': 40}
}
# Rearrage as per the eye_color
eye_color_dict = defaultdict(list)
for p, val in person.items():
	color = val.get('eye_color', 'Unknown')
	eye_color_dict[color].append(p)

print('eye_color_dict1: ', eye_color_dict)

person_2 = {
	'jack': defaultdict(lambda: 'Unknown', age=20, eye_color='blue'),
	'mack': defaultdict(lambda: 'Unknown', age=25, eye_color='black'),
	'mike': defaultdict(lambda: 'Unknown', age=30, eye_color='brown'),
	'michael': defaultdict(lambda: 'Unknown', age=35),
	'dean': defaultdict(lambda: 'Unknown', age=40)
}
# Rearrage as per the eye_color
eye_color_dict = defaultdict(list)
for p, val in person_2.items():
	eye_color_dict[val['eye_color']].append(p)

print('eye_color_dict2: ', eye_color_dict)

# Using Partial instead of going with 'defaultdict()' for every element
from functools import partial

# partial(defaultdict, lambda:'unknown') == lambda *args, **kwargs: defaultdict(lambda: 'unknown', *args, **kwargs)
eyedict = partial(defaultdict, lambda:'unknown')

person_3 = {
	'jack': eyedict(age=20, eye_color='blue'),
	'mack': eyedict(age=25, eye_color='black'),
	'mike': eyedict(age=30, eye_color='brown'),
	'michael': eyedict(age=35),
	'dean': eyedict(age=40)
}
eye_color_dict = defaultdict(list)
for p, val in person_3.items():
	eye_color_dict[val['eye_color']].append(p)
print('eye_color_dict3: ', eye_color_dict)


print("\n--------------------- 'Count number of times a function is called and the 1st call' Example ---------------------\n")

from collections import defaultdict, namedtuple
from datetime import datetime
from functools import wraps

def function_stats():
	d = defaultdict(lambda: {"count": 0, "first_called_at": datetime.utcnow()})
	Stats = namedtuple('Stats', 'decorator data')

	def decorator(fn):
		@wraps(fn)
		def wrapper(*args, **kwargs):
			d[fn.__name__]['count'] += 1
			return fn(*args, **kwargs)

		return wrapper

	return Stats(decorator, d)

stats = function_stats()
print('What is available in stats now:\n', stats.decorator, '\n', stats.data)

# Now, 'stats.decorator' is the decorator to be used.

@stats.decorator
def func1():
	pass

@stats.decorator
def func2():
	pass

@stats.decorator
def func3():
	pass

# Calls
func1()
func2()
func3()
func1()
func2()
func2()
pprint('\nFunction call Data: ', stats.data)