'''
NAMEDTUPLE is a function (not a type)
It generates new classes (new types)
It is a CLASS_FACTORY

The classes that get generated from namedtuple, inherits Tuple.
It also provides named properties to access the elements of Tuple

class_name_to_return = namedtuple('<class_name_to_return>', [list of fields for namedtuple])
'''
from collections import namedtuple

Point2D = namedtuple('Point2D', ['x','y'])

pt2d = Point2D(20,30)

# _fields is a class property to give us the fields of the named tuple.
print('Fields:',pt2d._fields)

# field_names -> namedtuple == Keys -> Dictionary
# VERYYYYY USEFUL: if pt2d is returned from a function, we returned multiple values from the fucntion.
print('x:',pt2d.x)
print('y:',pt2d.y)

#_asdict() will make the namedtuple into a dictionary
print(pt2d._asdict())

print('----------------------------------Modify NamedTuple----------------------------------')

print('Old Object:',id(pt2d))
# Simple pt2d.x = 5 WON'T work. It is a Tuple.
# _replace offers that service. MAKE SURE that KEYWORD match.
# this is a new tuple now.
pt2d = pt2d._replace(y=50)
print('New Object:',id(pt2d))
print(pt2d._asdict())

print('---Extend NamedTuple and add retain old values---')

# Get the old fields and create a new tuple
# new_fields = pt2d._fields + ('z',)
Point3D = namedtuple('Point3D', pt2d._fields + ('z',))

# Retain Old Values
pt3d = Point3D(*pt2d, 70)
print('3d:',pt3d._asdict())
# OR use _make.
print('3d, with make:', pt3d._make(pt2d+(70,)))

print('----------------------------------Doc_String----------------------------------')

# there are default doc_Strings that can be changed
print('Class Doc_string:',Point3D.__doc__)
print('Paramter Doc_String:', Point3D.z.__doc__)
Point3D.x.__doc__ = 'x coordinate'
Point3D.y.__doc__ = 'y coordinate'
Point3D.z.__doc__ = 'z coordinate'
print('Paramter Doc_String:', Point3D.z.__doc__)

print('----------------------------------Default Values----------------------------------')
# Use any that will increase the READABILITY of your code.
# Prototyping: Create 'zero' object and use _replace() to create the desired pointer

Point = namedtuple('Point', ['x1', 'x2', 'y1', 'y2', 'origin_x', 'origin_y'])
pt_zero = Point(x1=0, x2=0, y1=0, y2=0, origin_x=0, origin_y=0)
# Now the actual 'Point' objects to use
pt = pt_zero._replace(x1=2, y1=2, x2=5, y2=5)
print('Prototype Object:', pt_zero._asdict())
print('Actual Object:', pt._asdict())

''' __defaults__: func.__default__ is the actual Built-in method the assign values to Keyword arguments on function call.
Eg:
def func(a, b=10, c=20):
	pass

func.__defaults__ = (10,20) -> will do the same thing. Read it right to left and assign values to arguments.
'''

Point_def = namedtuple('Point_def', ['x1', 'x2', 'y1', 'y2', 'origin_x', 'origin_y'])
# Set Defaults for only origin_x and origin_y
Point_def.__new__.__defaults__ = (0,0)
# Now the actual 'Point' objects to use
pt = Point_def(2,2,5,5)
print('Actual Object with defaults:', pt._asdict())

print('----------------------------------Dictionary -> NameTuple----------------------------------')

dic = dict(key1 = 100, key2 = 200, key3 = 300)
print('Dictionary:', dic)

NT = namedtuple('NT', dic.keys())
# This will unpack value in the order they appear in the dictionary,
# but if the key order change while created namedtuple, the values will mismatch.
nt = NT(*dic.values())
print('NamedTuple with normal unpack:',nt)

# USE THIS: This will unpack the values as per the keys and No matter what version of python is there, mismatch WON't happen
nt_2 = NT(**dic)
print('NamedTuple with Keyword unpack:',nt_2)

print('----------------------------------List of Dictionary -> NameTuple----------------------------------')

l_d = [
		{'key1':1, 'key2':2},
		{'key1':3, 'key2':4},
		{'key1':5, 'key2':6, 'key3':7},
		{'key1':8}
	]
print('List of Dictionaries:', l_d)

# Get all the keys: set comprehension: can be in jumbled order
keys = {key for dict_ in l_d for key in dict_.keys()}
print('Keys in the list of dictionaries:',keys)

# Define a namedtuple and add default values to it.
NT_L = namedtuple('NT_L', sorted(keys))
NT_L.__new__.__defaults__ = (None,)*len(keys)

# Convert List of Dictionaries to Tuple
l_d_2_t = [NT_L(**dict_) for dict_ in l_d]
print('List of Dictionaries to Tuple:', l_d_2_t)