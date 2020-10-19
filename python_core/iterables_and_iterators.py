'''
Built-in functions that returns:

Iterables (returns a new iterator everytime we iterate over it): range(), dict.items(), dict.values(), dict.keys()

Iterators (returns itself everytime we iterate it.): zip(), open(file), enumerate
'''

# find out if a return type is iterable or iterator
r = range(5)
print('Type:', type(r))
iter_m = '__iter__' in dir(r)
print('Does it implement __iter__:', iter_m)
next_m = '__next__' in dir(r)
print('Does it implement __next__:', next_m)
if iter_m and next_m:
	print('Iterator')
elif iter_m and not next_m:
	print('Iterable')
else:
	print('Suspense... Will learn about this soon.')
print('Test: Should run multiple times')
print('Run 1: ', end='\t')
for i in r:
	print(i, end='\t')
print('\nRun 2:', end='\t')
print([i for i in r])

print('\nMost basic test -> iter(r) is r: ',iter(r) is r)

print('---------------------------------------------------')

r = zip([1,2,3,4], 'abcd')
print('Type:', type(r))
iter_m = '__iter__' in dir(r)
print('Does it implement __iter__:', iter_m)
next_m = '__next__' in dir(r)
print('Does it implement __next__:', next_m)
if iter_m and next_m:
	print('Iterator')
elif iter_m and not next_m:
	print('Iterable')
else:
	print('Suspense... Will learn about this soon.')
print('Test: Should not run multiple times')
print('Run 1: ', end='\t')
for i in r:
	print(i, end='\t')
print('\nRun 2:', end='\t')
print([i for i in r])

print('\nMost basic test -> iter(r) is r: ',iter(r) is r)

print('---------------------------------------------------')

r = enumerate('abcde')
print('Type:', type(r))
iter_m = '__iter__' in dir(r)
print('Does it implement __iter__:', iter_m)
next_m = '__next__' in dir(r)
print('Does it implement __next__:', next_m)
if iter_m and next_m:
	print('Iterator')
elif iter_m and not next_m:
	print('Iterable')
else:
	print('Suspense... Will learn about this soon.')
print('Test: Should not run multiple times')
print('Run 1: ', end='\t')
for i in r:
	print(i, end='\t')
print('\nRun 2:', end='\t')
print([i for i in r])

print('\nMost basic test -> iter(r) is r: ',iter(r) is r)

print('---------------------------------------------------')

r = {'a': 1, 'b': 2, 'c': 3}
print('Type:', type(r))
iter_m = '__iter__' in dir(r)
print('Does it implement __iter__:', iter_m)
next_m = '__next__' in dir(r)
print('Does it implement __next__:', next_m)
if iter_m and next_m:
	print('Iterator')
elif iter_m and not next_m:
	print('Iterable')
else:
	print('Suspense... Will learn about this soon.')
print('Test: Should run multiple times')
print('Run 1: ', end='\t')
for i in r:
	print(i, end='\t')
print('\nRun 2:', end='\t')
print([i for i in r])

print('\nMost basic test -> iter(r) is r: ',iter(r) is r)