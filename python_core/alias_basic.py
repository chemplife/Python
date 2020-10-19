'''
Enumeration Members are supposed to be UNIQUE.. Even the values

class Color(enum.Enum):
	Red = 1
	Green = 1
	Blue = 2

	-> Should not work.
	-> But it Does.. Because of Alias.

	-> There are only 2 Enumeration Memebrs at this point
		-> Color.Red 		and 		Color.Blue
		-> Color. Read and Color.Blue are called as 'Master Enumeration Members'
		-> Rest are Alias
			-> They point to the Enumeration Members
				-> Color.Green will point to Color.Red
				-> Colot.Green is Color.Red	==> True
'''

import enum

class Color(enum.Enum):
	Red = 1
	Green = 1
	Violet = 1
	Blue = 2
	Yellow = 2
	Orange = 3

print('Enumeration Members here: ', list(Color))
print('Get Color.Green..: ', Color.Green)
print('Is Green and Red Same: ', Color.Green is Color.Red)
# How to see the Aliases then?..
print('__members__ of the Enumeration: ', Color.__members__)

print('\n')

# To Enforce No Aliases use: @enum.unique decorator
# This will throw an error
try:
	@enum.unique
	class Color(enum.Enum):
		Red = 1
		Green = 1
		Blue = 2
except Exception as ex:
	print('Exception while creating Alias Enumeration: ', ex)