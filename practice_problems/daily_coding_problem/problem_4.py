'''
Date: 10/01/2020
Level: Hard
This problem was asked by Stripe.

Given an array of integers,
find the first missing positive integer in linear time and constant space.
In other words, find the lowest positive integer that does not exist in the array.
The array can contain duplicates and negative numbers as well.

For example,
the input [3, 4, -1, 1] should give 2.
The input [1, 2, 0] should give 3.

You can modify the input array in-place.
'''

lst = [3, 4, -1, 1]
print('Id of input list: ', id(lst))
# 'in' for list() -> O(n)
lst.append(ele for ele in lst if not ele < 0)
print('Id of input list later: ', id(lst))
if (min(lst)-1) > 0:
	print(min(lst)-1)
else:
	minimum = min(lst)
	# this can be non-linear..
	for i in range(1, len(lst)+1):
		if minimum+i not in lst:
			print(minimum+i)

