'''
Exercise-1: Do Exercise-3 from Code_Exercise-1, but using 'Counter' Object

Exercise-2: If given a list of 'eye_colors' and a list of 'Person' objects with a property of 'eye_color', create a list that has Number of people with
			each 'eye_color'.

Exercise-3: Given 3 files (common.json, prod.json, dev.json). Write a function that take a single argument (env_name) and returns a combined dict, by
			merging the 2 dicts from the files together, with the 'env settings' overriding any 'common settings' and filling in the gaps that are not
			in 'Common.json' file.
			Use 'Chainmap'..
'''

#### Exercise-1
from collections import defaultdict, Counter

def sort_dict_by_value(compose, reverse=False):
	return dict(sorted(compose.items(), key=lambda x: x[1], reverse=reverse))

ds1 = {'python': 10, 'java': 3, 'c#': 8, 'javascript': 15}
ds2 = {'java': 10, 'c++': 10, 'c#': 4, 'go': 9, 'python': 6}
ds3 = {'erlang': 5, 'haskell': 2, 'python': 1, 'pascal': 9}

# Current Solution
def freq_dict_default_dict(*args):
	ds = defaultdict(int)
	for dic in args:
		for key, value in dic.items():
			ds[key] +=value
	return sort_dict_by_value(ds, reverse=True)

print('DefaultDict: ', freq_dict_default_dict(ds1, ds2, ds3))

# Using Counter
# It will just add whatever the value of the key in current Counter object, with the value in the new dict
def freq_dict_counter(*args):
	ds = Counter()
	for dic in args:
		ds.update(dic)
	return dict(ds.most_common())
print('Counter: ', freq_dict_counter(ds1, ds2, ds3))

print('------------------------------------------------------------------\n')
#### Exercise-2
eye_colors = ('amber', 'blue', 'brown', 'gray', 'green', 'hazel', 'red', 'violet')

class Person:
	def __init__(self, eye_color):
		self.eye_color = eye_color

from random import seed, choices
seed(0)
persons = [Person(color) for color in choices(eye_colors[2:], k = 50)]

print('----------- Way 1 -----------')
# way 1: Using 'eye_colors' and create a dict from the values in 'counts' dict..
counts = Counter(p.eye_color for p in persons)
result = {color: counts.get(color, 0) for color in eye_colors}
print('Way 1: ', result)

print('----------- Way 2 -----------')
# way 2: Pre-initialize all color_count to '0' on 'Counter' object and just update the values
counts = Counter({color: 0 for color in eye_colors})
counts.update(p.eye_color for p in persons)
print('Way 2: ', dict(counts))


print('------------------------------------------------------------------\n')
#### Exercise-3

import json
from pprint import pprint
from collections import ChainMap


def load_settings(env):
	with open(f'exercise_files/{env}.json') as f:
		settings = json.load(f)
	return settings

# When we have nested dictionaires and we need to do ChainMap on each level.
def chain_recursive(d1, d2):
	# ChainMap(arg1, arg2)		-> 'arg1' values will take president over 'arg2' values..
	chain = ChainMap(d1, d2)
	for k, v in d1.items():
		if isinstance(v, dict) and k in d2 and isinstance(d2[k], dict):
			chain[k] = chain_recursive(d1[k], d2[k])
	return dict(chain)

# Function to create a merged settings file
def settings(env):
	common_settings = load_settings('common')
	env_settings = load_settings(env)
	return chain_recursive(env_settings, common_settings)

prod = settings('prod')
dev = settings('dev')
print('Prod: ', prod)
print('\nDev: ', dev)