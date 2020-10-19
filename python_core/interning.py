import sys

a = 'this_can_be_an_identifier'
b = 'this_can_be_an_identifier'
print(a is b)

c = 'Hello World Maxie'
d = 'Hello World Maxie'
print(c is d)

a = sys.intern('Ratul Aggarwal')
b = sys.intern('Ratul Aggarwal')
print(a is b)
print(id(a))
print(id(b))

'''
Intern: Add something to the Python cache.
- This makes:
		1. Comaprison faster: checking if variables point to same memory address is faster
		2. Memroy Optimization: In case of Natural Language Processing, this helps
		3. Startup slows down: Due to large cache, it slows the startup, so BE MINDFUL
'''