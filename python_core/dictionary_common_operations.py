'''
.get(), .update(), .value(), etc are built-in Functions written in 'C'. We cannot override them using classes.

however, getting values of a dictionary object like d[key] calls __getitem__(), which can be overriden. Look into 'userdict.py'
'''

d = dict(zip('abc', range(1,4)))
print('Dictionary: ', d)

print('\nGetting item by Key')
print("d['a']: ", d['a'])

# d[key] will cause KeyError if 'key' is not in dictionary. So, use get()	*************************
print("\nd.get('p'): ", d.get('p'))
print("Get default if key not present: ", d.get('p', 'N/A'))

# Membership testing: check if key is in dictionary.
print("\nIs 'z' in Dictionary: ", 'z' in d)

# Delete key-value
del d['a']
print("\nDictionary after Deletion: ", d)

# Deleting Key that is not present will cause KeyError. So, use Pop(key, default_value) ************
result = d.pop('b')
print(f'Dictionary after pop: {d}\nValue popped: {result}')

result = d.pop('z', 'N/A')
print(f'Dictionary after pop: {d}\nValue popped: {result}')

d2 = dict({str(i):i**2 for i in range(1,5)})
print('\nNew Dictionary to work with: ', d2)

# popitem(), returns a tuple of (key, value) from the BOTTOM of the dictionary
# popitem() = LIFO operation (like Stack)
# When dictioanry is empty: popitem() raise KeyError.	*********************************************

result = d2.popitem()
print(f'Dictionary after popitem: {d2}\nValue popped: {result}')


# d.setdefault(key, value): will return the 'value' at key, if key is present in the dictionary.
# else, it will create an enter with the key, value that is provided in setdefault.
print(f"\nAdd key-value if key is not present: {d2.setdefault('5', 50)},\tNew dict: {d2}")

print(f"Return the value without modification: {d2.setdefault('5', 100)},\tNew dict: {d2}")

print('\n\n----------- Clear Dictionary -----------')
print('D and ID of D:', d, '\t',id(d))
d = {}
print('D and ID of D:', d, '\t',id(d))
# For 'd', we just assigned an empty dictionary to it and created a NEW assignment. This is NOT clearing dictionary

# d2.clear() : mutates the dictionary.
print('D2 and ID of D2:', d2, '\t',id(d2))
d2.clear()
print('D2 and ID of D2:', d2, '\t',id(d2))


print('\n\n--------------------------------- Dictionary Views ---------------------------------')
'''
d.keys()	-> Give all the keys 					-|
d.values()	-> Give all the Values 					 |-> Produce an ITERABLE. So, we need to iterate through it to see items.
d.items()	-> Give all (key,value) pair as tuple	-|									Eg: list(d.keys())

keys() -> will behave as a set() because all the values are unique
items() -> can behave as a set() depending on values being immutable or mutable. Mutable values will not allow item() to be a set type.

Set() behavior means: operations like union (|), intersection (&) are possible
'''

d = {'a':1, 'b': 2, 'c':3, 'd': 4}
d2 = {'a':5, 'b': 6, 'c':7, 'e':8}
# we want to have have dictionary that have only uncommon parts of 'd' and 'd2'

# Way 1: Linear way.
union = d.keys() | d2.keys()
intersection = d.keys() & d2.keys()
keys = union - intersection
result = {}
for key in keys:
	result[key] = d.get(key) or d2.get(key)
print('Result dictionary: ', result)

# Way 2: Dictionary comprehension
# ^ operator = symmetric difference between sets.
result_dc = {key: (d.get(key) or d2.get(key)) for key in d.keys()^d2.keys()}
print('Result Dictionary with Dict_comprehension: ', result_dc)


print('\n\n------------------------ Dictionary: Updating/Merging/Copying ------------------------')
'''
Update: 3 forms-
		-> d1.update(d2): 		update dictionary based on the key/value pair of another dictionary
		-> d1.update(iterable):	Iterable should have iterable in (key, value) form.
								-> We can have List_Comprehension, Generator, Generator_Expression, anything that gives out iterable.
		-> d1.update(kwargs):	argument-name = Key ; argument-value = value
'''
print('------ Updating ------')

d1 = {'a':1, 'b': 2, 'c':3, 'd': 4}
d2 = {'a':5, 'b': 6, 'c':7, 'e':8}
print('D1: ', d1)
print('D2: ', d2)
print('\n')
print("Updated D1 Dict with D2 Dict: ", d1.update(d2))
print("Updated D1 Dict with Kwargs: ", d1.update(b=20, f=30))
print("Updated D1 Dict with iterable: ", d1.update([('c', 15), ['g', 17]]))

print('------ Merging ------')
print('Merging D1 and D2 Dicts: ', {**d1, **d2})

print('------ Copying ------')
# from copy import deepcopy
# print('-- Shallow Copy --')
# # Shallow copy: New containers with keys/values still referenced from the key/value-addresses where the original Dict got it.
# d1_copy = d1.copy()
# d2_copy = {**d2}
# d1_copy_2 = dict(d1)
# d2_copy_2 = {k:v for k,v in d2.items()}
# print(f'D1: {d1}\nD1_copy: {d1_copy}\nD1_copy_2: {d1_copy_2}')
# print('\n')
# print(f'D2: {d2}\nD2_copy: {d2_copy}\nD2_copy_2: {d2_copy_2}')

# print('-- Deep Copy --')
# # Deep copy: New containers with keys/values not referenced from the original Dict.
# deep_d1 = d1.deepcopy()
# print(f'D1: {d1}\nD1_deepcopy: {deep_d1}')


print('\n\n------------------------ Dictionary: Deleting Elements ------------------------')
'''
Regular set operations of pop() and del() works with dictionary exactly the same way.
But we cannot del() or insert() -> Alter the length of the Dictionary
	while iterating over the dictionary.
	-> But we can do it if we make the views (keys(), items()) static. Like list(d.keys()).
		-> New we can do pop, del()

** popitem() -> No need to create a static sequence of the view because view is not required.
'''
d = {'a': 1, 'b': 2, 'c': 3}
print('Dictionary: ',d)
for k in list(d.keys()):
	v = d.pop(k)
	print(k, v**2)
print('Dictionary after pop: ', d)

d = {'a': 1, 'b': 2, 'c': 3}
print('\nDictionary: ',d)
for k,v in list(d.items()):
	print(k, v**2)
	del d[k]
print('Dictionary after del: ', d)

d = {'a': 1, 'b': 2, 'c': 3}
print('\nDictionary: ',d)
for _ in range(len(d)):
	k,v = d.popitem()
	print(k,":",v)
print('Dictionary after popitem: ', d)

d = {'a': 1, 'b': 2, 'c': 3}
print('\nDictionary: ',d)
while len(d) > 0:
	k,v = d.popitem()
	print(k,":",v)
print('Dictionary after while popitem: ', d)