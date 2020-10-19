'''
Hash Functions: A function that maps from a set(domain) of arbitrary size to another smaller set of fixed size.
									h:D->R		where X(R) < X(D)

Hash Table / Hash Map:
		Basic premise of Hash Table: We have an array of indices,
		and we have a hash function that calculates index inside that array based on a key that is passed in.

Dictionary are stored in memory as Hash Table.
	-> For each 'value' there is 1 unique 'key'.
	-> each time we call a 'key', same value should show up.

Storing a key/value pair:
	-> calculate a hash key [h(key)]: returns an index value
	-> we will store the 'Value' at that index.
	-> To Lookup a 'Value' by 'Key':
		-> Pass the key to the same 'Hash Function' [h(key)], and we get the unique index back
		-> Return the 'Value' from that index.
			-> Range of indices should be definite positive number
			-> generated index for expected input values to be uniformly distributed (as much as possible)

	- Realistically, we don't want the generated indices to be grouped together very closely, because otherwise, the index value
		returned for 2 different Keys can be same. So, we try to spread out our hash map over the range of indices as much as possible.
	- But that will require a big range to store fewer Key/Value pairs.
	- So, the idea to have a unique index for every key is dropped, and the event where 2 keys have same index returned by
		hash function is called as 'Collision'

Eg of Hash function: h(key, range):
						h('john', 11):
							return len(key)%range

Dealing with Collisions:
	1. Chaining: Store multiple values at the same index. Like, having Lists-of-Lists.
					-> This is still more efficient, looking for a value in a smaller list
							as compared to looking in 1 big List-of-Lists.

	2. Probing: Calculate hash value (index) for 1 key, and than start filling the rest of the Keys in remaining Indices sequencially.
				-> Eg: h('alexander', 5): 948 % 5 = 3.
					-> Probe Sequence = 3,4,0,1,2							So, ['alexander', 'Alexander'] 	=> 3
					-> For 'john' 		=> probe Sequence = 1,2,3,4,0		So, ['john', 'John'] 			=> 1
					-> For 'eric' 		=> probe Sequence = 4,0,1,2,3		So, ['eric', 'Eric'] 			=> 4
					-> For 'michael' 	=> probe Sequence = 3,4,0,1,2		So, ['michael', 'Michael'] 		=> 0 (Since 3 & 4 = taken)
					-> For 'graham'		=> probe Sequence = 4,0,1,2,3		so, ['graham', 'Graham'] 		=> 2 (Since 4,0,1 = taken)

		Both Index (hash value) and probe sequence, both are taken into consideration to remove collision.
		-> So, a Key must generate the same sequence of valid indices (probe sequence).
		
		While looking up the Hash Map for Value of the Key, we:
			1. Look at the hash value and follow the sequence.
				Eg: Find 'alexander'-> hash value = 3, probe sequence = 3,4,0,1,2	-> is 'alexander' at 3 = Yes	-> Return
					Find 'michael'	-> hash value = 3, probe sequence = 3,4,0,1,2	-> is 'michael' at 3 = No
																					-> is 'michael' at 4 = No
																					-> is 'michael' at 0 = Yes		-> Return

KEY SHARING  - PEP412
	-> Creates Split-table dictionaries: Make multiple instances of the same class to provide more efficient storage
		-Eg: name: ['john', 'eric', michael]
			 age:  [78, 75, 80]

			 Instead of having separate dictionaies for 'john', 'eric', and 'michael'

Compact Dictionaries:
	-> The Values are stored in a separate list: Value=[[hash value address (index address), key, value]]
		-> Order of elements in 'Values List' == Order in which they are entered.
		-> That is why Dictionary Order is guaranteed to be the same as entered (after Python 3.5)
	-> Indices for each element is stored separately.

Built-in hash():
	-> Always return an integer value
	-> if key1 == key2, than hash(key1) == hash(key2)
	-> Python truncates the hashes into some fixed size (sys.hash_info.width) : Depends on is the python is 32 or 64 bit & system bits
	-> Only immutable types are 'HASHABLE', we cannot hash a 'LIST' or 'SET'.
		-> Because immutable object's values won't change and thus their probe sequence won't change.
		-> So, if the hash changes, it changes the starting postion for the probe sequence,
			and we end up looking at the wrong index for the value of key/value pair.
		-> Eg:
			-> map(hash, (1,2,3,4))				-> gives 4 int values (HASHABLE)
			-> map(hash, (1.1, 1.2, 2.5))		-> gives 3 int values (HASHABLE)
			-> map(hash, ('hello', 'python'))	-> gives 2 int values (HASHABLE)
			-> hash((1,2,3,4))					-> gives 1 int value (HASHABLE)
			-> hash([1,2,3])					-> NOT HASHABLE

		-> Functions are immutable types too, so they can be used as Keys in dictionary as well.
		-> ForzenSets are immutable so, can be used for Dictionary Keys.

		-> Thus, a 'SET' or 'LIST' cannot be used for Dictionary Keys.
			-> In case of custom objects, we can but we need to make sure that the Hash of the object does not change.
				-> Basically, do not mutate the Key otherwise the hash will change and dict lookup will not give you
					the value from the key, even if the key is there in the dict.
						-> Check custom_classes_and_hashing.py for eg.
'''

print('Hash Value of Tuple: ',hash((1,2,3)))
#Tuple of all immutable elements is Hashable

d1 = {(1,2,3):'This is a tuple'}
print('Type: ', type(d1))
print('D1: ', d1)
print(f'Value of {d1.keys()}: ', d1[(1,2,3)])

# Hash values equality
print('\n--------------- Hash Equality ---------------')
t1 = (1,2,3)
t2 = (1,2,3)

print('t1 is t2?: ', t1 is t2)
print('t1 == t2?: ', t1 == t2)
print('hash(t1) == hash(t2)?: ', hash(t1)==hash(t2))