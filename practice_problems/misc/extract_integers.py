'''
Make a tuple with all integer values from the given list.

Input = [1, 2, 3, [4, 5], 6, 7, (8, 9, 10), {'a':(20, 30, 40)}]
Output = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 20, 30, 40)
'''

# Brute Force
def get_tuple(lst):
	temp_lst = []
	for ele in lst:
		if isinstance(ele, int):
			temp_lst.append(ele)

		elif isinstance(ele, list):
			temp = get_tuple(ele)
			for t in temp:
				temp_lst.append(t)

		elif isinstance(ele, tuple):
			temp = get_tuple(ele)
			for t in temp:
				temp_lst.append(t)

		elif isinstance(ele, dict):
			for key, val in ele.items():
				temp = get_tuple(val)
				for t in temp:
					temp_lst.append(t)

	return tuple(temp_lst)


inp_list = [1, 2, 3, [4, 5, [11, 12]], 6, 7, (8, 9, 10), {'a':(20, 30, 40), 'b': [13, 14, 'c']}]
print('List:', get_tuple(inp_list))