print('------------------ Reverse using Slicing ------------------')
print('-------------- way 1 --------------')
seq = [3,2,4,1,5,6]
print(f'Seq: {seq}')
for i in seq[::-1]:
	print(i, end='\t')
print('\n')

'''
This is wasteful: 	1) Creates a new sequence in reverse and iterate over it.
					2) You might be needing only few elements, now you have the whole sequence 2 times.
'''

print('-------------- way 2 --------------')
for i in range(len(seq)-1,-1,-1):
	print(seq[i], end='\t')
print('\n')

'''
Messy Syntax
'''

print('------------------ Reverse SEQUENCE TYPE using reversed() ------------------')
print(f'Seq: {seq}')
for i in reversed(seq):
	print(i, end='\t')
print('\n')

'''
It doesn't create a copy
It creates an iterator that iterated backwards over the SEQUENCE.
If we are creating a custom iterator that goes in reverse, we need:
																	-> __getitem__
																	-> __len__
We can override __reversed__ in our customer iterator.

revered(): won't work on general ITERABLES.
		-> The way, iter() looks for __iter__ first and if doesn't find one, try for __getitem__
		-> reversed() looks for __reversed__ first, and if doesn't find one, try for __getitem__ & __len__
'''


