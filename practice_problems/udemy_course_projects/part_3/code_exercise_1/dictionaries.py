'''
Exercise-1: sort dictionary based on 'values'

Exercise-2: Given 2 dictionaries 'd1' & 'd2'. Create 'd3' having only common keys from 'd1' & 'd2', and 'value' being tuple of values from 'd1' & 'd2'.

Exercise-3: There are 3 dictionaies with frequency data. Create 1 dictionary that have all the data from original 3 & 'total freq' as value of
			the common keys. Order new dictionary from hightest-lowest frequency.
			(Hint: Function should take variable number of dictionaries and compute the resulant dictionary..)

Exercise-4: Given 3 Dictionaries. Get all the keys that are not present in all 3 dictionaries and the tuple values of them in all 3 dictionaries.
'''

#### Exercise 1

compose = {'Johann': 65, 'Ludwig': 56, 'Frederic': 39, 'Wolfgang': 35}
def sort_dict_by_value(compose, reverse=False):
	return dict(sorted(compose.items(), key=lambda x: x[1], reverse=reverse))
print(sort_dict_by_value(compose))


#### Exercise 2
print('------------------------------------------------------------------')
d1 = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
d2 = {'b': 20, 'c': 30, 'y': 40, 'z': 50}
d = {key: (value, d2[key]) for key, value in d1.items() if key in d2}
print(d)

# OR
def intersection(d1, d2):
	d1_key = d1.keys()
	d2_key = d2.keys()
	keys = d1_key & d2_key
	return {k:(d1[k], d2[k]) for k in keys}

print(intersection(d1, d2))


#### Exercise 3
print('------------------------------------------------------------------')
from collections import defaultdict

ds1 = {'python': 10, 'java': 3, 'c#': 8, 'javascript': 15}
ds2 = {'java': 10, 'c++': 10, 'c#': 4, 'go': 9, 'python': 6}
ds3 = {'erlang': 5, 'haskell': 2, 'python': 1, 'pascal': 9}

def freq_dict(*args):
	ds = defaultdict(int)
	for dic in args:
		for key, value in dic.items():
			ds[key] +=value
	return sort_dict_by_value(ds, reverse=True)

print(freq_dict(ds1, ds2, ds3))
print(freq_dict(ds1, ds2))


#### Exercise 4
print('------------------------------------------------------------------')

n1 = {'employees': 100, 'employee': 5000, 'users': 10, 'user': 100}
n2 = {'employees': 250, 'users': 23, 'user': 230}
n3 = {'employees': 150, 'users': 4, 'login': 1000}

def uncommon_key_track(*args):
	union, intersection = args[0], args[0]
	for dic in args[1:]:
		union = union | dic.keys()
		intersection = intersection & dic.keys()
	relevent = union - intersection
	n = defaultdict(list)
	for dic in args:
		for key in relevent:
			n[key].append(dic.get(key, 0))
	return {k:tuple(v) for k,v in n.items()}

print(uncommon_key_track(n1, n2, n3))