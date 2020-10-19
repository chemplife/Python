import ctypes

a = [1,2,3]
# id(variable) = address where the variable is pointing at.
print(hex(id(a)))
c = a
# this will tell how many variables are pointing at an address.
print(ctypes.c_long.from_address(id(a)).value)

'''
GARBAGE COLLECTOR: Cleans circular references and prevents memory leaks
- Version 3.4 and up: it works fine.
- Version 2.7 for example: if circular reference has distructor (__del__()),
						   it marks the circular ref objects as 'uncollectables'.
'''