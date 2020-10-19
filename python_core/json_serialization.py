'''
JSON: JavaScript Object Notation.
Default: Serialization/Deserialization will not execute code so, it is consider safe compared to pickling/unpickling

Datatype supported: "string"	-> Double Quotes Delimiter	And Unicode characters only.
					Numbers		-> 100, 3.14, 3.14e-05, 3.14E+5		-> all are considered floats. No distinctions
					Boolean		-> true, false						-> No double quotes "true". That would be considered string
					Array		-> [1,3.14, "python"]				-> Ordered. Like List.
					Dictionary	-> {"a":1, "b": "abc"}				-> Keys = Strings,	values = Any supported Datatype; UNORDERED
					Empty Value -> null

		***	Non-Standard Datatypes that are supported
				integer			-> 100
				floats 			-> 100.0, 3.14, NaN, Infinity, -Infinity

JSON Dictionaires:
	{
		"Pascal" : [ 
            {
            	"Name"  : "Pascal Made Simple",
            	"price" : 700
            },
            { 	"Name"  : "Guide to Pascal",
            	"price" : 400
            }
        ],
        "Scala"  : [
            { 	"Name"  : "Scala for the Impatient",
            	"price" : 1000
            }, 
            { 	"Name"  : "Scala in Depth",
            	"price" : 1300
            }
        ]    
    }

JSON Dictionaries:		Strings
Python Dictionaries:	Objects

import json

Methods: dump, dumps, load, loads

Dict ----(Serialize using Dump/Dumps)----> File String ----(DeSerialize using Load/Loads)----> Dict

Problems:
1. Json Keys must be Strings 				-> Python Keys needs to be hashable. (Can be of type other than strings)
2. Json Value Datatypes are limited 		-> Python values can be of any datatype.
3. Even if we Serialize these different datatypes using custom classes, how to deserialize them

For the mentioned problems, we need to have CUSTOM Serializers/Deserializers 
'''

import json

d1 = {'a': 100, 'b': 200}
d1_json = json.dumps(d1)

print('Type of d1: ', type(d1))
print('D1: ', d1)
print('Type of d1_json: ', type(d1_json))
print('D1_json: ', d1_json)
#d1_json is string and keys are double quotes.

#Like pretty_print pprint() for dicts, we can do indent for json
print('pretty_print json:\n',json.dumps(d1,indent=2))

d2 = json.loads(d1_json)
print('Type of d2: ', type(d2))
print('D2: ', d2)
print('Is D1 == D2: ', d1==d2)
print('Is D1 same object as D2: ', d1 is d2)

print('\n\n------------------ Integer Keys ------------------')

d1 = {1: 100, 2: 200}
d1_json = json.dumps(d1)

print('D1: ', d1)
print('D1_json: ', d1_json)
#d1_json is numerical keys converted to strings in double quotes.

d2 = json.loads(d1_json)
print('D2: ', d2)
print('Is D1 == D2: ', d1==d2)
# Because the Keys of D2 are Strings and D1 Keys are numbers.

print('\n\n------------------ Value Datatypes ------------------')
d_json = {'a':(1,2,3)}
ser = json.dumps(d_json)
deser = json.loads(ser)
print('Initial dict: ', d_json)
print('Deserialized dict: ', deser)
print('Is serialized dict and DeSerialized output equal: ', d_json==deser)
# Tuple got converted to List. JSON doesn't know TUPLE

print('\n\n------------------ Bad JSON ------------------')

from decimal import Decimal

d_json = '''{"a":(1,2,3)}'''
print('Initial dict: ', d_json)
try:
	deser = json.loads(d_json)
except Exception as exc:
	print(f'Got Exception: {exc}')

d_ser = {'a': 10, 'b': Decimal(10.234)}
print('\nInitial dict: ', d_ser)
try:
	ser = json.dumps(d_ser)
except Exception as exc:
	print(f'Got Exception: {exc}')


print('\n\n------------------ Custom Serialization ------------------')

class Person:
	def __init__(self, name, age):
		self.name = name
		self.age = age

	def __repr__(self):
		return f'Person(name={self.name}, age={self.age})'

p = Person('John', 82)
print('Person Object: ', p)
try:
	print('\nJSON serialized', json.dumps({'John':p}))
except Exception as exc:
	print(f'Got Exception: {exc}')

# To make Person class Object serializable, we need to implement toJSON() method
class Person_2:
	def __init__(self, name, age):
		self.name = name
		self.age = age

	def __repr__(self):
		return f'Person(name={self.name}, age={self.age})'

	#Python will call this function to get a serializable object.
	def toJSON(self):
		# or use
		# return vars(self)
		return dict(name=self.name, age=self.age)

p_2 = Person_2('John', 82)
print('\nPerson_2 Object: ', p_2)
try:
	print('JSON serialized:\n', json.dumps({'John':p_2.toJSON()}, indent=2))
except Exception as exc:
	print(f'Got Exception: {exc}')

'''
dumps(default=func)
When JSON Encoder encounters a type that it doesn't know how to encode,it looks for a
		-> CALLABLE function in its DEFAULT argument
			-> CALLABLE function takes 1 argument.
'''
from datetime import datetime

current = datetime.utcnow()
print('\n\nDatetime Object: ', current)
try:
	print('JSON serialized:\n', json.dumps(current))
except Exception as exc:
	print('Got Exception: ', exc)

#Custom Format Function
def format_iso(dt):
	return dt.strftime('%Y-%m-%dT%H:%M:%S')
#or
#current.isoformat()

log_record = {'Time1': datetime.utcnow().isoformat(),
				'message': "This is test",
				'Time2': format_iso(current)
			}

try:
	print('JSON serialized:\n', json.dumps(log_record, indent=2))
except Exception as exc:
	print('Got Exception: ', exc)

log_record = {'Time1': datetime.utcnow(),
				'message': "This is test",
				'Time2': current
			}

try:
	print('JSON serialized with Default:\n', json.dumps(log_record, indent=2, default=format_iso))
except Exception as exc:
	print('Got Exception: ', exc)

# Custom Formatter to be used as Default
def json_custom_formatter(arg):
	if isinstance(arg, datetime):
		return arg.isoformat()

	elif isinstance(arg, set) or isinstance(arg, tuple):
		return list(arg)

	elif isinstance(arg, Decimal):
		return float(arg)
	elif isinstance(arg, Person_2):
		return arg.toJSON()

log_record_2 = {'Time': datetime.utcnow(),
				'message': "This is test",
				'types': {'a', 1, 1.34, Decimal(1.12)},
				'tval': (1,2,3, Decimal(3.456))
			}

try:
	print('\n\nJSON serialized with custom formatter:\n', json.dumps(log_record_2, indent=2, default=json_custom_formatter))
except Exception as exc:
	print('Got Exception: ', exc)


from functools import singledispatch
from fractions import Fraction
# MAKE the Custom Formatter MORE GENERIC
# Custom Formatter to be used as Default
# We can use singledispatch here to register more datatype support as well.
@singledispatch
def json_custom_formatter(arg):
	if isinstance(arg, datetime):
		return arg.isoformat()

	elif isinstance(arg, set) or isinstance(arg, tuple):
		return list(arg)

	elif isinstance(arg, Decimal):
		return float(arg)

	else:
		try:
			return arg.toJSON()
		except AttributeError:
			try:
				return vars(arg)
			except TypeError:
				return str(arg)

@json_custom_formatter.register(Fraction)
def _(arg):
	return f'Fraction({str(arg)})'

#Now, Fraction is also covered in the json_custom_formatter() function.