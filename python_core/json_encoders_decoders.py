'''
JSONEncoder class instance is being used by Python to Serialize Data.
JSONEncoder class has same methods that are used by json.dumps() function. Like
															-> Default:			Use custom callable to format unsupported datatypes
															-> indent:			indent for human readability
															-> separators:		Select separators in dict, like ',' or ':'
															-> sort_keys:		Make dict sequence intact when converting to JSON
															-> skipkeys:		Skip Key and keep serializing data if some keys are of
																				unsupported datatypes.

Most of the arguments available in Dumps/Dump function are available in the instance of JSONEncoder class as well.

Dump/Dumps has a 'cls' argument that is NOT available in JSONEncoder class
- This allows us to specify our custom JSONEncoder class for dump/dumps function to use for doing the encoding.
- By default, the arguments passed in dump/dumps function are used to initialize the default JSONEncoder class, and
'cls' allows us to make the function to use the passed arguments to initialize our custom JSONEncoder class.

Why Custom JSONEncoder required?
- When we have many json.dump/dumps statements and we need to have specific values for all these arguments, it is easy to miss/wrongly
assign values to some of them.
- So, putting all that in 1 place and putting 1 thing as argument is easy way to manage the program-wide formatting.

How to make a custom JSONEncoder class?
- Subsclass the original JSONEncoder class, and customize the initializer to the parent class (basically send our own arguments to the
initializer of the parent class.)
	-> We can override 'Default Method' of JSONEncoder class & take control to give same results that we got from 'Default Argument'.
		-> In essence, we can either handle unsupported datatypes on dumps(default) argument level,
			OR at the JSONEncoder.Default method level. (default argument feeds its value to this Default method to do the actual work)

	-> We can only define how to serialize the datatypes that Default JSONEncoder does not know how to handle.
		-> We cannot override Default JSONEncoder serialization for 'String', 'int' or any other datatype that it knows how to handle.
'''

print('--------------------------------------------- Encoding / Serializing ---------------------------------------------\n')

import json
from datetime import datetime

class CustomJSONEncoder(json.JSONEncoder):
	# overloading the Default Method of the JSONEncoder Parent class.
	# we can overload this because by default, JSONEncoder doesn't handle this datatype.
	def default(self, arg):
		if isinstance(arg, datetime):
			return arg.isoformat()
		else:
			# Deligate it back to the parent class to handle this scenario
			super().default(arg)

custom_encoder = CustomJSONEncoder()
print("***** Different things our custom encoder will format for us. *****\
	\n***** It only uses the 'Default' method fo custom functionality to handle 'DATETIME' object. *****\
	\n***** Rest all the method calls goes directly to the parent class methods. *****\n")

print('custom_encoder.encode(Tuple): ', custom_encoder.encode((1,2,3,4)))
print('custom_encoder.encode(Number): ', custom_encoder.encode(10))
print('custom_encoder.encode(datetime): ', custom_encoder.encode(datetime.utcnow()))

print('\n\n--------------- Using CustomJSONEncoder for Serializing ---------------\n')

# With 'cls' argument, Python will take care of creating an instance of our CustomJSONEncoder class.
ser = json.dumps(dict(name='John', time=datetime.utcnow()), cls=CustomJSONEncoder)
print('Custom_encoder serialized json: ', ser)

print('\n\n--------------- Changing Default Initializer of JSONEncoder ---------------\n')

# Removing white-spaces to create more compact JSON.
class CustomJSONEncoder_2(json.JSONEncoder):
	def __init__(self, *args, **kwargs):
		# We can changes these values in any way we want, in the dumps argument, hardcode them in the kwargs, anywhere.
		print('All the kwargs fo JSONEncoder initialization:\n', kwargs)
		# indent is None by default
		# allow_nan = blocks any not_a_number elements to be serialized. Languages like JAVA will throw error with this JSON.
		super().__init__(skipkeys=True,
						 allow_nan=False,
						 separators=(',',':')
						)

	def default(self, arg):
		if isinstance(arg, datetime):
			return arg.isoformat()
		else:
			super().default(arg)

d = {
	'time': datetime.utcnow(),
	1+2j : 'Complex number',
	(1,2): 'Tuple',
	1: 'Number',
	'a': (1,2,3)
}
# Complex and tuple keys will not get serialized.

print('\nEncoded json: ', json.dumps(d, cls=CustomJSONEncoder_2))

print('\n\n--------------- Default method of JSONEncoder and Serialization ---------------\n')
# We can do anything we want with datatypes that are not handled by json.JSONEncoder

class CustomJSONEncoder_3(json.JSONEncoder):
	def __init__(self, *args, **kwargs):
		super().__init__(indent=2)

	def default(self, arg):
		if isinstance(arg, datetime):
			obj = dict(
					datatype='DATETIME',
					iso=arg.isoformat(),
					date=arg.date().isoformat(),
					time=arg.time().isoformat(),
					year=arg.year,
					month=arg.month,
					day=arg.day,
					hour=arg.hour,
					minutes=arg.minute,
					seconds=arg.second
				)
			return obj
		else:
			# Deligate it back to the parent class to handle this scenario
			super().default(arg)

print('datetime custom default:\n', json.dumps({'time':datetime.utcnow()}, cls=CustomJSONEncoder_3))


print('\n\n--------------------------------------------- Decoding / Deserializing ---------------------------------------------\n')
'''
Decoding is the reverse process for JSON encoding and get the data formatted back from 'JSON strings' to 'Python Objects'
To do it, there is an 'object_hook' argument in json.loads().
	-> Object_hook: takes a callable as value which will be called for every dictionary in the JSON String.
	Steps:
		-> json.loads(): will parse the JSON as Dictionary called as 'Root Dictionary'
		-> Object_hook callable(): Will be called for Every dictionary in the 'Root Dictionary'. It will be called for
									Root Dictionary as well in the very end.


Schemas: A Pre-Defined Structure as per whihc the JSON will get serialized.
		- We can create a custom Deserializer based on the Schema.
		- Schema can be for the entire JSON, or for a sub-component of the JSON only.

Object_hook: Allow to customize Deserialization of Objects only (like Dictionaries). But not for int, float datatypes.
			It passes the Deserialized Dict to the callable as argument get a Python Dict object back.
			It recursively gets called for all the JSON Objects to handle the Deserialization.


For that, loads() have other arguments:
		-> parse_float		-|-> We can provide custom callables for any of these,
		-> parse_int		 |-> This callable will take 1 argument (which will be a string from JSON).
		-> parse_constant	-|-> we return the value that we want to return.

** There are No overrides for 'Strings'.

Object_pairs_hook: Only one from 'Object_hook' and 'Object_pair_hook' can be used at a time in loads() argument.
					If both of them are used, 'Object_hook' will get ignored.

While JSON Dict does not guarantee the Order, the deserialization does not guarantee the order in which the Dict is going to come out.
So, one way to fix it: Pass the Dict to callable as a List of Tuple containing Key/Value pair.
This will preserve the order from JSON to Python Dict.

Object_hook() 			-> Argument is a dictionary 		-> NOT Guaranteed to be in the same order as JSON
Object_pairs_hook()		-> Argument is a List-of-Tuples		-> Guaranteed to be in the same order as JSON

** Object_hook / Object_pairs_hook receives Parsed Dictionaries. Meaning, parse_float, parse_int.. callables are called first before
	calling the function in Object_hook / Object_pairs_hook.


'''

import json
from decimal import Decimal
from datetime import datetime
from fractions import Fraction

def make_decimal(arg):
	return Decimal(arg)

sample_json = '''{"a": 100.5, "b": 3}'''
print('Sample Json: ', sample_json)
print('Decoded Dict: ', json.loads(sample_json, parse_float=make_decimal))

# Creating Simple Schema to handle Datetime Decoding
print('\n\n------------------ Creating Simple Schema ------------------\n')

dt_json_1 = '''{
	"time" : "2018-10-21T09:14:00",
	"message": "Test String."
}'''

print('Simple Json: ', dt_json_1)
# Datetime Object will come out as string.
print('Decoded Json: ', json.loads(dt_json_1))

# Schema based encoded json

dt_json_2 = '''{
	"time" : {
		"objecttype": "datetime",
		"value": "2018-10-21T09:14:00"
	},
	"message": "Test String."
}'''
# Now, we need to deserialize it based on the objecttype.
dt_json_2_deser = json.loads(dt_json_2)

for key, value in dt_json_2_deser.items():
	if (isinstance(value, dict) and
		'objecttype' in value and
		value['objecttype'] == 'datetime'
	):
		dt_json_2_deser[key] = datetime.strptime(value['value'], '%Y-%m-%dT%H:%M:%S')

print('Decoded Json with Datetime Schema: ', dt_json_2_deser)

# Example 2 of Schema 

dt_json_3 = '''{
	"share" : {
		"objecttype": "fraction",
		"numerator": 1,
		"denominator": 8
	},
	"Cake": "Chocolate Cake."
}'''
# Now, we need to deserialize it based on the objecttype.
dt_json_3_deser = json.loads(dt_json_3)

for key, value in dt_json_3_deser.items():
	if (isinstance(value, dict) and
		'objecttype' in value and
		value['objecttype'] == 'fraction'
	):
		num = value['numerator']
		den = value['denominator']
		dt_json_3_deser[key] = Fraction(num,den)

print('Decoded Json with Fraction Schema: ', dt_json_3_deser)


# Creating Custom Decoder for object_hook
print('\n\n------------------ Custom Decoder and Object_hook ------------------\n')

print('Just to see the sequence of custom_decoder_call\n')

def custom_decoder(arg):
	print('Decoding: ',arg)
	return arg

json_obj = '''
{
	"a": 1,
	"b": 2,
	"c": {
		"c.1": 1,
		"c.2": 2,
		"c.3": {
			"c.3.1": 1,
			"c.3.2": 2,
			"c.3.PO": "May The Force Be With You." 
		}
	}
}
'''
print('Decoding JSON Obj:', json.loads(json_obj, object_hook=custom_decoder))

# Custom_Decoder for dt_json_2 to handle Datetime
def custom_decoder_dt(arg):
	if 'objecttype' in arg and arg['objecttype']=='datetime':
		return datetime.strptime(arg['value'], '%Y-%m-%dT%H:%M:%S')
	# This else is very important. Otherwise when Custom_Decoder is called for Root dict and it will return None.
	else:
		return arg

print('Decoding Datetime JSON Obj:', json.loads(dt_json_2, object_hook=custom_decoder_dt))

# Custom_Decoder for dt_json_3 to handle Fraction
def custom_decoder_fr(arg):
	if 'objecttype' in arg and arg['objecttype']=='fraction':
		num = arg['numerator']
		den = arg['denominator']
		return Fraction(num,den)
	# This else is very important. Otherwise when Custom_Decoder is called for Root dict and it will return None.
	else:
		return arg

print('Decoding Fraction JSON Obj:', json.loads(dt_json_3, object_hook=custom_decoder_fr))

# Generic Custom_Decoder Function
def custom_decoder_gen(arg):
	return_val = arg
	if 'objecttype' in arg:
		if arg['objecttype'] == 'datetime':
			return_val = datetime.strptime(arg['value'], '%Y-%m-%dT%H:%M:%S')
		elif arg['objecttype'] == 'fraction':
			return_val = Fraction(arg['numerator'],arg['denominator'])
		elif arg['objecttype'] == 'decimal':
			return_val = Decimal(arg['value'])
	return return_val

json_obj_nested = '''
{
	"a": 1,
	"b": {
		"objecttype": "decimal",
		"value": "10.2353452436245624343145315"
	},
	"c": {
		"c.1": 1,
		"time" : {
			"objecttype": "datetime",
			"value": "2018-10-21T09:14:00"
		},
		"c.3": {
			"c.3.1": 1,
			"share" : {
				"objecttype": "fraction",
				"numerator": 1,
				"denominator": 8
			},
			"c.3.PO": "May The Force Be With You." 
		}
	}
}
'''

print('Decoding using Generic Custom_Decoder:\n', json.loads(json_obj_nested, object_hook=custom_decoder_gen))


# Creating Custom Decoder for object_pairs_hook
print('\n\n------------------ Custom Decoder and Object_pairs_hook ------------------\n')

def custom_pairs_decoder(arg):
	print('Decoding: ',arg)
	return arg

def custom_pairs_decoder_dict_out(arg):
	print('Decoding: ',arg)
	return {k:v for k, v in arg}

json_obj_pair = '''
{
	"a": 1,
	"b": 2,
	"c": {
		"c.1": 1,
		"c.2": 2,
		"c.3": {
			"c.3.1": 1,
			"c.3.2": 2,
			"c.3.PO": "May The Force Be With You." 
		}
	}
}
'''
print('Decoding JSON Obj with tuple pairs:\n', json.loads(json_obj, object_pairs_hook=custom_pairs_decoder))
print('\n')
print('Decoding JSON Obj with Dict Return:\n', json.loads(json_obj, object_pairs_hook=custom_pairs_decoder_dict_out))


print('\n\n--------------- Using Custom_JSONDecoder for Deserializing ---------------\n')
'''
Unlike JSONEncoder, which gets called for only those parts of the Dictionary Object that is not handled by the Default_JSONEncoder,
JSONDecoder gets the entire JSON string to handle.
'''

json_doc = '''
{
	"a": 100,
	"b": [1,2,3],
	"c": "python",
	"d": {
		"e": 4,
		"f": 5.5
	}
}
'''

class CustomJSONDecoder(json.JSONDecoder):
	def decode(self, arg):
		print('JSONDecoder Called:')
		return arg

print('Custom_JSONDecoder class, try 1: ', json.loads(json_doc, cls=CustomJSONDecoder))

''' We can customize it in any way.
decode() function can be made to:
	-> do general decodeing first by json.loads() and work on each element that follows the endcoding schema.
	-> Search for a schema pattern in the whole json string and if there is a match, then we run the json.loads() and perform
		operations it.
'''

##### NEED to ADD Code here #####