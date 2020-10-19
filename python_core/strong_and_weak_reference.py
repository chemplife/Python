'''
Strong Reference:
	-> References that are counted towards the 'Reference Count' of an object.
	-> Regular referencing that we know till this point are all 'Strong References'
	-> 'Strong Reference Count' needs to be 0 before Garbage Collector clears the memory.

Weak References:
	-> References that does not count towards the 'Reference Count' of an object.
	-> Since this does not effect the 'Reference Count' of the object, Garbage Collector is not concerned about the Weak Reference Count.

** We cannot create 'Weak Reference' for any Built-in Types.
	Eg: List, Dictionary, tuple, etc...
'''

import weakref
import ctypes


def ref_count(address):
	return ctypes.c_long.from_address(address).value

class Person:
	pass

# Strong Reference
p1 = Person()
p1_id = id(p1)
# Weak Reference
p2 = weakref.ref(p1)
print('Reference Count: ', ref_count(p1_id))
# p2 is a callable. (even if the object 'p1' not a callable.)
# return the original object 'p1'
# 'None' is return if 'p1' is garbage collected

# If we do this, it will create another Strong Reference to the Original Object.
p3 = p2()
print('Reference Count check: ', ref_count(p1_id))

'''
If we want to use 'Weak References' as Keys in a dictionary (like we are going to do in descriptors_basics.py file.)
we can use 'WeakKeyDictionary' from 'weakref' for that.
'''

p4 = Person()				# Strong Reference
d = weakref.WeakKeyDictionary()
d[p4] = 'some value'		# a weak reference is used for the 'Person' instance (for Keys)

del p4						# No more 'Strong References' so, it is Garbage Collected

# items are automatically removed from the Weak-Key-Dictionary

# to count the number of 'Weak References'
print('Weak reference count: ', weakref.getweakrefcount(p1))

# In reality, Python is keeping track of Weak references in 'obj.__weakref__'.. it is a Linked-List
print('Weak reference Linked-List: ', p1.__weakref__)


# Rules to Creating a WeakKeyDictionary:
# 1. The Original object for Weak Reference needs to be an object for which a Weak Reference can be created..
#	Eg: a custom-class-object is elidgible, but string-object is not
#
# 2. The Original object for Weak Reference needs to be Hashable.
#	Eg: if a class implements '__eq__()' method, the '__hash__()' needs to be implemented to make the class-objects hashable.
#		Because '__eq__()' make the 'defualt __hash__()' of the class-object a NoneType.


'''
__weakref__ is a data-descriptor for a class..
'''
print('\nPerson Class dict: ', Person.__dict__)
print('__weakref__ has __get__?: ', hasattr(Person.__weakref__, '__get__'))
print('__weakref__ has __set__?: ', hasattr(Person.__weakref__, '__set__'))