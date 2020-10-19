'''
Different ways to create dictionaries.

** Read hashmap_hashfunctions.py for background info
'''

print('------------- Way 1: Using Literals -------------')
d1 = {'k1':100, 'k2':200}
print('Type: ', type(d1))
print('D1: ', d1)


print('\n------------- Way 2: Using dict() -------------')
#'Keys' need to be a string type
d2 = dict(k1=100, k2=200)
print('Type: ', type(d2))
print('D2: ', d2)

print('-*--*--*--*--*--*--*--*--*--*--*-')
#Using iterable-of-iterables. Now, keys other than string works.
d3 = dict([('a', 100), ['x', 200], {3,300}])
print('D3: ', d3)

print('-*--*--*--*--*--*--*--*--*--*--*-')
print('-- Copy Dictionary --')
d4 = {'a': [1,2,3], 'b': {1:100, 2:200}}
d = dict(d4)
print('Copies Dictionary (d): ',d)
print('d4 is d?: ', d4 is d)
# This is SHALLOW COPY: Means id(d) != id(d4), but d['k1'] == d4['k1'] (It just copied the reference of key-value in d.)
#						So, modifying mutable key-value of 'd' will modify 'd4' as well.
#						Modifying immutable key-value of 'd' will NOT modify 'd4'.

print("d4['a'] is d['a']?: ", d4['a'] is d['a'])
d['a'].append(1000)
d['b'][3] = 3000
print('Modified d: ', d)
print('Modified d4: ', d4)

#add new key-value, won't change originally referenced objects
print('-- Add new key to d --')
d['c'] = 10
print('Modified d: ', d)
print('Modified d4: ', d4)
print("d4['a'] is d['a']?: ", d4['a'] is d['a'])

print('\n------------- Way 3: Using zip of iterables -------------')
#'Keys' need to be a string type
l_value = [1,2,3,4]
t_key = ('a', 'b', 'c', 'd')
d5 = {}
for k, v in zip(t_key,l_value):
	d5[k] = v
print('Type: ', type(d5))
print('D5: ', d5)

print('-*--*--*--*--*--*--*--*--*--*--*-')
d6 = {k:v for k,v in zip(t_key,l_value)}
print('D6 using Dictionary comprehension: ', d6)

s_key = 'abcd'
r_value = range(1,5)
print('D7 usinng Dictionary comprehension + conditions: ', {k:v for k,v in zip(s_key, r_value) if v%2==0})


print('\n------------- Way 4: Using dict.fromkeys() -------------')

# dict.fromkeys(iterable, initial_value)

d8 = dict.fromkeys([1,2,3,4], 'N/A')
print('Type: ', type(d8))
print('D8: ', d8)

d9 = dict.fromkeys('abcd', 0)
print('D9: ', d9)

d10 = dict.fromkeys('python')
print('D10: ', d10)