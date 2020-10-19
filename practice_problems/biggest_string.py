'''
Problem 1: Find the biggest substring in the string that has only 2 unique characters
Input: assdeeeddfffhf
Output: deeedd

Problem 2: Find the longest word that has the input characters.
Input: {'act', 'acquaintance', 'trace'}
chars: cat
Output: acquaintance
'''

#### Problem 1:
inp_str = 'assdeeeddfffhf'

# Brute Force
# Char_lst => [char1, char2, length]





#### Problem 2:
lst = ['act', 'acquaintance', 'trace']
inp = 'cat'
inp_lst = list(inp)
largest = lst[0]

# Bruce Force Solution
for l in lst:
	count = 0
	for i in inp_lst:
		if i in l:
			count += 1
		if count == len(inp_lst):
			if len(largest) < len(l):
				largest = l
print(largest)


# Optimized Solution
hash_lst = set()
for i in inp_lst:
	hash_lst.add(hash(i))

# Add Caching to optimize it more..
for l in lst:
	temp = list(l)
	temp_set = set()
	for t in temp:
		temp_set.add(hash(t))
	if hash_lst.issubset(temp_set) and len(largest) < len(l):
		largest = l
print(largest)