'''
Reduce:
Takes 1 iterable and returns single value
Like, max, min, sum, product, factorial, etc

reduce(func, iterable, initializer=optional to override start value of 1st element)

Partial:
Help reduce the number of arguments to pass in a function

Operators:
Helper Class for mathematical operations
Returns a 'CALLABLE' and do Partial operation to reduce parameters.
'''
from functools import reduce, partial

print('--------------Reduce--------------')
l = [1,2,3,4,5,9,10]
pr = reduce(lambda x,y: x*y, l)
print('Product:',pr)

a= 3
fac = reduce(lambda x,y: x*y, range(1,a+1))
print('Factorial:',fac)

print('--------------Partial--------------')
def myfunc(a,b,*args,k,l,**kwargs):
	print(f'a:{a}, b:{b}, args:{args}, k:{k}, l:{l}, kwargs:{kwargs}')

f1 = partial(myfunc, 10,k=5,o=100)
f1(20, 30,40,50,l=5, m=7, n=9)

def pow(base, exponent):
	return base**exponent

sq = partial(pow,exponent=2)
cu = partial(pow,exponent=3)
print(f'Square of 5 = {sq(5)}')
print(f'Cube of 5 = {cu(5)}')

# The deffinition fix agrument problem.
# exponent pointing at address content of z still points there because it got fixed at the time of function definition.
z = 10
expo = partial(pow, exponent=z)
print(f'Problem Try 1: {expo(2)}')
z = 5
print(f'Problem Try 2: {expo(2)}')

print('--------------Operators--------------')
import operator

# -Get 2nd element of any list
# -f is callable that needs a iterable to get 1st element of.
# -attrgetter works the same way, except, it gets a particular attribute for any callable.
# -methodcaller works the same way for functions, except with attrgetter, we would do () at the end to run the function.
# 	with methodcaller, we don't have to add () at the end to run it. 
f = operator.itemgetter(1)
l = [1,2,3,5,6]
s = 'python'
f_2 = operator.itemgetter(1,3,4)
print('List 2nd element',f(l))
print('String 2nd element',f(s))
print('List multiple elements',f_2(l))
print('List multiple element',f_2(s))