from datetime import datetime
print(datetime.utcnow())

def log(msg, *, dt=datetime.utcnow()):
	print(f'Log:{msg} at time:{dt}')

# this will return dt same for both name1 and name2.
'''
******
when log function is defined, time at that moment is stored in dt and does not change.

MINDFUL: Immutable Parameter set in function definition doesn't change.
	  -  Mutable parameters will not be fixed. 

Basically,
	def log(msg, *, dt=datetime.utcnow()) -> this line get fully evaluated at the time of definition

******
'''
print('Fixed Parameter')
log('name 1')
for n in range(20000000):
	pass

log('name 2')
print('------------------------------')

print('Not Fixed Parameter')
def log2(msg, *, dt=None):
	dt = dt or datetime.utcnow() 
	print(f'Log:{msg} at time:{dt}')

log2('name 3')
for n in range(20000000):
	pass

log2('name 4')
print('------------------------------')

# Mutable Object will change.
# To make it fixed, use immutable objects, like Tuple
print('UnFixed List Example')
mylist = [1,2,3]
def list_func(a=mylist):
	print('list:',mylist)

list_func()

mylist.append(4)
list_func()
print('------------------------------')
