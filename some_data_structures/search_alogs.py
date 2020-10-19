# Binary Search.. Most commonly asked in Coding interview through some example.
def binary_search(lst, num, start=None, stop=None):
	lst = sorted(lst)
	if start == None and stop == None:
		start = 0
		stop = len(lst) - 1
	
	if stop <= start:
		return 'Not Found'

	mid_index = (start + stop) // 2
	if lst[mid_index] == num:
		return mid_index
	elif lst[mid_index] > num:
		return binary_search(lst, num, start=start, stop=mid_index-1)
	else:
		return binary_search(lst, num, start=mid_index+1, stop=stop)

if __name__ == "__main__":
	num_list = [12, 15, 17, 19, 21, 24, 45, 67]
	num = 45
	print(f'Find {num}: ', binary_search(num_list, num))
