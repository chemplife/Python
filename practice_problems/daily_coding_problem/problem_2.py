'''
Date: 09/29/2020
Level: Hard
This problem was asked by Uber.

Given an array of integers,
return a new array such that each element at index i of the new array is the
product of all the numbers in the original array except the one at i.

For example,
if our input was [1, 2, 3, 4, 5],
the expected output would be [120, 60, 40, 30, 24].
If our input was [3, 2, 1],
the expected output would be [2, 3, 6].

Follow-up: what if you can't use division?
'''

lst = [1, 2, 3, 4, 5]
n_list = []
# Brute Force Solution: using 3 lists
# No division
for val in lst:
	temp_lst = [l for l in lst if l != val]
	new_val = 1
	for t in temp_lst:
		new_val *= t
	n_list.append(new_val)

print(n_list)

# Optimized Solution: using 2 lists
# No division
n_list = []
for val in lst:
	new_val = 1
	for v in lst:
		if v != val:
			new_val *= v
	n_list.append(new_val)
print(n_list)