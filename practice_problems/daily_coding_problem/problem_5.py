'''
Date: 10/02/2020
Level: Medium
This problem was asked by Jane Street.

cons(a, b) constructs a pair, and car(pair) and cdr(pair) returns the first and last element of that pair.
For example, car(cons(3, 4)) returns 3, and cdr(cons(3, 4)) returns 4.

Given this implementation of cons:

def cons(a, b):
    def pair(f):
        return f(a, b)
    return pair

Implement car and cdr.
'''

#####################
#
#	Problem doesn't state anything about the parameter of pair(f)
#	which needs to be a function.
#
#	** CAUTION: 'cons()'' is not a decorator here.. It does return a Closure but does not take a 'function' as parameter.
#	
#####################

def cons(a, b):
    def pair(f):
        return f(a, b)
    return pair


fn = cons(3, 4)
# fn = pair
# f is a function-> f(a, b)

def func(a, b):
	return (a, b)

def car(fn):
	t = fn(func)
	return t[0]

def cdr(fn):
	t = fn(func)
	return t[1]

print('car():', car(fn))
print('cdr():', cdr(fn))
print('\nSame as\n')
print('car():', car(cons(3, 4)))
print('cdr():', cdr(cons(3, 4)))