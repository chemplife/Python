a = [1,2,3]
print(id(a))

# Keeps the address

# append need 1 element
a.append(4)
print(f"'a' after append: {a}")
print(id(a))

#extend require an iterable
a.extend({10,11,12})
print(f"'a' after extend: {a}")
print(id(a))

a[0] = 'a'
print(f"'a' after replacing value: {a}")
print(id(a))

a[0:2] = (5,6,7,8)
print(f"'a' after slice addition: {a}")
print(id(a))

# insert(<target index>, <element>)
a.insert(3,20)
print(f"'a' after index insert: {a}")
print(id(a))

# del list[index]
del a[4]
print(f"'a' after element delete: {a}")
print(id(a))

# inplace reverse
a.reverse()
print(f"'a' after inplace reverse: {a}")
print(id(a))

# this will change the address of new 'a'
a = a[::-1]
print(f"'a' after reverse by slice: {a}")
print(id(a))

print('\n\n--------------------- Copy ---------------------')
# copy() creates shallow copy: b, b1 will have different address, but 'b[0] is b1[0]' == True (elements have same addresses) 
b = [[1,2,3], 4, 5]
print(f'List b: {b}')
print(id(b))

b1 = b.copy()
print(f'Copy of List b: {b1}')
print(id(b1))

print('Addresses of elements:')
print(f'Element 0: {id(b[0])}')
print(f'Element 0: {id(b1[0])}')
print(f'Element 1: {id(b[1])}')
print(f'Element 1: {id(b1[1])}')

b[0].append(8)
print(f'List b after element 0 append: {b}')
print(f'Copy of List b after element 0 append: {b1}')

# BAD IDEA
# Copy first before reversing a mutable object.
def reverse(lis):
	# Copy will create a new object but the elements have same address
	l = lis.copy()
	# reverse will do an in-place reversal on the newly created object.
	# the individual elements still have the same address.
	# But if we change any mutable element in the copy, it WILL change the mutable element at the address in the original too.
	# It WILL NOT change any immutable element in the original if the copy is changed.
	l.reverse()
	return l
s = [1,2,3,4]
print(f'list s: {s}')
s_1 = reverse(s)
print(f'reverse of list s: {s_1}')
print(f'list s afterwards: {s}')


# Reverse a Tuple
t = (1,2,3,4)
t_1 = t[::-1]
t_2 = tuple(reversed(t))
print(t_1)
print(t_2)