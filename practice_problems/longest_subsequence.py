'''
Find the length of the longest subsequence of increasing numbers.
Inp: '30641475'
Out: 4
=> subsequence of increasing numbers: 0, 1, 4, 7
'''

# Brute Force
def get_seq(seq):
	larg_seq = []
	max_len = 0
	for ind in range(len(seq)):
		ind_lst = [ind]
		val = seq[ind]
		for x in range(ind+1, len(seq)):
			if seq[x] > val:
				ind_lst.append(x)

		if len(ind_lst) > max_len:
			max_len = len(ind_lst)
			larg_seq = ind_lst
		if (len(seq) - ind+1) < max_len:
			break
	return max_len, [seq[i] for i in larg_seq]


inp = '30641475'
print(get_seq(inp))