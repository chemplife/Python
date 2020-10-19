"""
sorted(iterable, key: <function>, reverse=False/True):
				1) makes a copy and does not mutate current object.
				2) ALWAYS RETURNS a LIST, no matter the type of input sequence.
				3) Uses TimSort for sorting.
	iterable: any sequence
	key: function that is given the element we are trying to sort.
	reverse: want ascending or descending

Natural Sort: Key on the basis of which we sort the element, is the element itself.
	- sorted(iterable) ---> sorted(iterable, key = lambda x: x)

Stable Sort: Maintaining relative order of elements that have equal sorting keys.

In-place Sorting: For mutable iterable
	- list have sort(): mutates the list
	- 
"""

# In-place sorting: ONLY for MUTABLE
l = [5,2,4,1,3]

print(f'Before Sorting\nList: {l}	ID: {id(l)}')
l.sort(reverse=True)
print(f'After Sorting\nList: {l}	ID: {id(l)}')

# Sorted Function
l = (5,2,4,1,3)
print(f'Before Sorting\nList: {l}	ID: {id(l)}		type: {type(l)}')
l2 = sorted(l)
print(f'After Sorting\nList: {l2}	ID: {id(l2)}		type: {type(l2)}')

# Sort dictionary based on the value
dic = {1:300, 2:100, 3:150}
print(f'dictionary: {dic}')
print(f'Sorted Dic: {sorted(dic, key=lambda x: dic[x])}')

print('''\n\n########################################################################################################################
######################################################### Part 2 #######################################################
########################################################################################################################\n''')