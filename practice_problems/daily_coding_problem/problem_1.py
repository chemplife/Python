'''
Date: 09/28/2020
Level: Easy
This problem was recently asked by Google.

Given a list of numbers and a number k, return whether any two numbers from the list add up to k.
For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.
'''

def check_sum(k, lst):
	for ele in lst:
		diff = k - ele
		# check if diff == ele; if yes, then if lst has 2 values equal to ele.
		if diff in lst:
			if diff == ele:
				if lst.count(ele) == 1:
					return False
			return True
	return False

k = 17
lst = [10, 15, 3, 7]
print('Result: ', check_sum(k, lst))