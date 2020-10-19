'''
Chainmap works the same way as chain() from itertools.
-> Chain map is to iteratre over multiple Dictionaries without copying them in 1 single Dict.
-> It is a realtime view like chain. Meaning, we can change the underlying dictionaries while iterating over them with Chainmap, and
	Cahinmap will iterate over the changes as well when it get to them.
-> Unlike Chain (which can't mutate the iterables while iterating through them), chainmap allows to mutate the underlying Dictionaries.

-> The resulting Chain from Chainmap is itself a dictionary. Meaning, there cannot be repeated 'Keys'
Eg: d1 = {'a':10, 'b':20, 'c':30}
	d2 = {'a':100, 'd':40, 'e':50}
	d3 = ChainMap(d1, d2)
	-> d3['b'] = 20
	-> d3['e'] = 50
	-> d3['a'] = 10 (unline in unpacking {**d1, **d2} where the last occurance takes effect, here 1st occurance takes effect.)

	d3 = {**d1, **d2}
	-> d3['a'] = 100

** ChainMap does not guarantee the Order of Keys.

ChainMap(d1,d2,d3,d4)

d1 = Child
d2,d3,d4 = parents

-> d.parents = Chain containing parent dictionaries.
-> d.new_child(d5) = Add d5 in the beggining of the ChainMap. (chainMap(d5,d1,d2,d3,d4))
	:Alternatively ==> chainMap(d5, chainMap(d1,d2,d3,d4))

.maps -> Returns a mutable list of all the dictionaries in chainMap
	  -> Order of this list is same as order in chainMap (parent and child are still in sequence)
	  -> List is modifiable
	  		-> d = ChainMap(d1,d2,d3)
			   d.maps => [d1,d2,d3]
			   d.maps.append(d4)	=> ChainMap(d1,d2,d3,d4)
			   d.maps.insert(0,d5)	=> ChainMap(d5,d1,d2,d3,d4)
			   del d.maps[1]		=> ChainMap(d5,d2,d3,d4)


Mutating the Dictionary Key/Value pair in ChainMap
-> Any Mutating operation only effects 'child' dict, not the rest
	d1 = {'a':10, 'b':20, 'c':30}
	d2 = {'a':50, 'e':60, 'b':70}
	d = ChainMap(d1,d2)
	
	d['a'] = 100	=> d1 = {'a':100, 'b':20, 'c':30}
	d['e'] = 40		=> d1 = {'a':10, 'b':20, 'c':30, 'e':40}
	del d['a']		=> d1 = {b':20, 'c':30, 'e':40}

	But since 'a' is in d2 as well,
	print(d['a'])	=> 50
	
	Deleting a Key that is not in 'Child' dict, will give 'KeyError'
'''

from collections import ChainMap


d1 = {'a':10, 'b':20, 'c':30}
d2 = {'a':100, 'd':40, 'e':50}

print('Unpacking: ', {**d1, **d2})
print('ChainMap: ', dict(ChainMap(d1,d2)))

# ChainMap is not of Dict instance. But behaves like Dict.
d = ChainMap(d1,d2)
print('Type of Chainmap: ', type(d))
print('IS Chainmap instance of Dict: ',isinstance(d,dict))
for k,v in d.items():
	print(k, " ", v)


d['z'] = 20
print('\nd after addition: ', d)
print('Mutated d1: ', d1)

d['e'] = 400
print('\nd after addition of existing Dict: ', d)
print('Mutated d1: ', d1)

del d['e']
print('\nPrint Deleted Value d[e]:', d['e'])

# ChainMap is a View. Any Change made in underlying dict will get reflected in Chainmap
d2.update({'m':5})
print('\nUpdated d2: ', d2)
print('Chainmap after d2 update: ', d)

# Adding Dicts to ChainMap
d3 = {'m':150, 'n':240, 'o':350}
# Way 1
d = ChainMap(d, d3)
print('\nPrint Added dict in ChainMap (end): ', d)

# way 2
d = ChainMap(d3, d)
print('\nPrint Added dict in ChainMap (front): ', d)

# way 3 == way 2
print('\nPrint Added dict in ChainMap new_child: ', d.new_child(d3))

print('\nPrint ChainMap of all dicts except 1st: ', d.parents)

print('\n\n--------------------- Maps ---------------------\n')

d1 = {'a':10, 'b':20, 'c':30}
d2 = {'a':100, 'd':40, 'e':50}
d3 = {'m':150, 'n':240, 'o':350}

d_maps = ChainMap(d1,d2)
print('ChainMap before append: ', d_maps)
d_maps.maps.append(d3)
print('\nChainMap after append: ', d_maps)

#Each Dict is an element in this list.
print('\nMaps List: ', d_maps.maps)

del d_maps.maps[0]
print('\nChainMap after del: ', d_maps)


print('\n\n--------------------- UseCase of Child-Only-Mutable-Feature ---------------------\n')
''' Config dict, that you want to get updated when dealing with a user, but comes back to the original after done processing

way 1: Do a 'deepcopy' of config dict. Use it and discard afte use.
		But this will lead to memory usage

way 2: Use ChainMap. Update empty 'Child dict' with the 'parent-config dict'
'''
config = {
	'host': 'prod.prac.com',
	'port': 5432,
	'database_url': 'prac',
	'user_id': '$pg_user',
	'user_pwd': '$pg_pwd'
}

local_config = ChainMap({}, config)
print('Local_Config:\n', list(local_config.items()))

local_config['user_id'] = 'test'
local_config['user_pwd'] = 'test'

print('Local_Config after change:\n', list(local_config.items()))
print('Local_Config ChainMap View:\n', local_config)

