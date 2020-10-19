"""
*******************************************************************************************************************
************* Before Moving on, go over 'In-place concatination / Mutation' part of iterable_test.py **************
*******************************************************************************************************************

Sequence operators can be made custom to create custom sequences:
Eg,
	__add__: 			obj3 = obj1 + obj2	operations
	__iadd__:			obj1 += obj2 		operations
	__mul__:			obj3 = obj1 * obj2	operations
	__imul__:			obj1 *= obj2		operations
	__radd__:			obj3 = obj2 + obj1	operations		(Right Add)
	__iradd__:			obj2 += obj1		operations		(In-place Right Add)
	__rmul__:			obj3 = obj2 * obj1	operations		(Right Multiplication)
	__irmul:			obj2 *= obj1		operations		(In-place Right Multiplication)
	__contains__:		'in'				operations

Right operations (radd, rmul, etc): Gets called if add, mul are not performable.
									Will still be performed in respect to obj2
	Eg: 
	obj1 = 3
	obj2 = 'abc'
	obj1 *= obj2 (3.__mul__('abc') is incorrect operation.)

	So, python calls, 'abc'.__mul__(3) to return 'abcabcabc'

Rules:
	Every sequnce generating class needs to have basic functionality methods:
	-> __len__: 			to return length of the sequence
	-> __getitem__: 		to return value on the requested index.
			-- **** NEED to have 'raise IndexError' to handle out of bound indices.
"""