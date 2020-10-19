def test(a,b):
	return a+10, b+10

x = 10
y = 20

# Function call pass ADDRESS as argument.
# After operation, a new value gets generated in different address.
# int, float, string, etc are immutable
print('Func val:',test(x,y))
print('x:',x)
print('y:',y)