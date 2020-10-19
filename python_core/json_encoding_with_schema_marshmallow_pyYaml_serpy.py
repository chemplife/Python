'''
How to Ensure that the JSON Encoding is being done as per a schema?
This become essential when writing our own custom JSONDecoder

-> Python DOES NOT have any in-built way to fix this. So, 3rd party tools are being used for this.
-> These 3rd Party tools not only help in defining Schema for Encoding, but they also help in Decoding the JSON as well.

For this doc, we will use the Schema-Standard mentioned in the documentation at https://json-schema.org

To make sure that the 'JSON String' is following our Schema, we use
'jsonschema' library
	-> pip install jsonschema

******** 'jsonschema' Library is just for VALIDATING the Schema. ********

And we can use Methods like,
	-> from jsonschema import validate
	-> from jsonschema.exceptions import ValidationError
	-> from json import loads, dumps, JSONDecodeError
'''
from jsonschema import validate
from jsonschema.exceptions import ValidationError
from json import loads, dumps, JSONDecodeError


# Schema Def.
'''
{
	"firstName": "...",
	"middleInitial": "...",
	"lastName": "...",
	"age": "..."
}
'''
# 'type = object' means 'person_schema' is going to be a dictionary. We can have 'List' as well.
# properties = they are the Keys of the Dictionary
person_schema ={
	"type": "object",
	"properties": {
		"firstName": {"type": "string"},
		"middleInitial": {"type": "string"},
		"lastName": {"type": "string"},
		"age": {"type": "number"},
	}
}
# Now, this doesn't mean that the 'JSON String':
#	-> cannot have other 'Keys' in it.
#	-> Needs to have all of the 'Keys' mentioned in the Schema
# The 'Keys' mentioned in Schema need to have the value of the mentioned 'Type', to be a valid 'JSON String' for this Schema

# Valid
p1 = {
	"firstName": "Ratul",
	"middleInitial": "",
	"lastName": "Aggarwal",
	"age": 1
}

# Valid
p2 = {
	"firstName": "Ratul",
	"age": -10.5
}

# Invalid
p3 = {
	"firstName": "Ratul",
	"middleInitial": "DC",
	"lastName": "Aggarwal",
	"age": "Unknown"
}

# Schema with more Rules
# properties = they are the Keys of the Dictionary
person_schema_2 ={
	"type": "object",
	"properties": {
		"firstName": {
			"type": "string",
			"minLength": 1
		},
		"middleInitial": {
			"type": "string",
			"maxLength": 1
		},
		"lastName": {
			"type": "string",
			"minLength": 1
		},
		"age": {
			"type": "number",
			"minimum": 0
		},
		"eyeColor": {
			"type": "string",
			# Eyecolor needs to be string but from the following lost only
			"enum": ["amber", "green", "red", "black", "blue"]
		},
		"address": {
			"type": "object",
			"properties": {
				"line_1": {
					"type": "string",
					"minLength": 5
				},
				"line_2": {
					"type": "string",
					# Minimum Length Not defined same as below
					#"minLength": 0
				}
			}
		}
	},
	# The Fields the are required, rest are Optional. By-Default, this list is empty, so everything is optional
	"required": ["firstName", "lastName"]
}

# Valid
p1_1 = {
	"firstName": "Ratul",
	"middleInitial": "",
	"lastName": "Aggarwal",
	"age": 1
}

# Invalid
p2_1 = {
	"firstName": "Ratul",
	"age": -10.5
}

# Invalid
p3_1 = {
	"firstName": "Ratul",
	"middleInitial": "DC",
	"lastName": "Aggarwal",
	"age": "Unknown"
}

json_doc = p1_1
print('JSON Object: ', json_doc)

try:
	validate(loads(json_doc), person_schema_2)
except JSONDecodeError as exc:
	print('Invalid Json: ', exc)
except ValidationError as exc:
	print('Validation Error: ', exc)
else:
	# if No error
	print('JSON is Valid and confirms to Schema')

# But for the invalid json like p2_1, exception will only give us the '1st' error that was encountered while checking the schema.
# For Validator to check for all the errors and give us the list, we do following

from jsonschema import Draft4Validator


validator = Draft4Validator(person_schema_2)

print('Error List is:')
for errors in validator.iter_errors(loads(json_doc)):
	print('errors', end="\n-----------\n")

print('\n\n-------------------------------------------- Marshalling using Marshmallow --------------------------------------------\n')
'''
Download marshmallow from
	-> https://marshmallow.readthedocs.io/en/3.0/

It not only does:
	-> Schema Validation for JSON
	-> Serailize / Deserialize Objects

*********** But It can also convert 1 object into Other Object.
			Like converting 1 Dictionary to another Dictionary
'''

from datetime import date
from marshmallow import Schema, fields

class Person:
	def __init__(self, firstName, lastName, dob):
		self.firstName = firstName,
		self.lastName = lastName,
		self.dob = dob

	def __repr__(self):
		return f'Person({self.firstName},{self.lastName},{self.dob})'

p1 = Person('John', 'Cleese', date(1988,2,20))
print('Person object: ', p1)

# For Deserializing, we NEED TO HAVE a schema for the JSON Document.
class PersonSchema(Schema):
	first_name = fields.Str()
	last_name = fields.Str()
	dob = fields.Date()

# Now, we can create a PersonSchema instance that can handle any 'Object' that has 'Firstname', 'Lastname', and 'dob'
person_schema = PersonSchema()

# Now, we can use the instance of PersonSchema (person_schema) to Serialize 'Objects' into 'JSON Strings'
print('Serialized Person Object as per schema: ', person_schema.dump(p1))
# Now, the output of this will be a 'MarshalResult' object
# >> MarshalResult(data={'last_name': 'Cleese', 'dob': '1988-2-20', 'first_name': 'John'}, errors={})
# 'data' and 'errors' are of type = Dict

# To get the Data Dictionary we want
print('Serialized Person Object Dictionary as per schema: ', person_schema.dump(p1).data)

# Now, we can serialize this 'Schema-Serialized-Dictionary-Obejct into 'JSON-String'
data = person_schema.dump(p1).data
print('JSON Serialize Dict Object: ', json.dumps(data))

# dumps() of Marshmallow will do the serialization that json.dumps() does.
print('JSON Serialize Dict Object by Marshmallow: ', person_schema.dumps(p1).data)

print('\n----------- serializing NamedTuple object instead of Dictionary Object -----------\n')
from collections import namedtuple

PT = namedtuple('PT', 'first_name, last_name, dob')
p2 = PT('Eric', 'Bana', date(1943, 10, 21))
print('NamedTuple: ', p2)
print('JSON Serialize NamedTuple: ', person_schema.dumps(p2).data)

# If we feed Data to the Schema that is not in the fields, Marshmallow serializer will Ignore it.
print('\n----------- Ignored Data -----------\n')
PT2 = namedtuple('PT2', 'first_name, last_name, age')
pt2 = PT2('Michael', 'The Arch-Angel', 500)
print('NamedTuple: ', pt2)
print('JSON Serialize NamedTuple with ignored data: ', person_schema.dumps(pt2).data)

print('\n\n-------------------------------------------- Selective Serializing --------------------------------------------\n')
'''
Selecting what fields we want in the Serialized Output.

Usecase:
	-> When Dealing with MongoDB, we might want to Omit the 'Object_ID' while Serialize the Data defore returning it to someone
'''
person_partial = PersonSchema(only=('first_name', 'last_name'))
print('Partial serializing: ', person_partial.dumps(p1).data)

# OR

person_partial_2 = PersonSchema(exclude=['age'])
print('Partial serializing: ', person_partial_2.dumps(p1).data)

print('\n\n-------------------------------------------- Complex Examples --------------------------------------------\n')

class Movie:
	def __init__(self, title, year, actors):
		self.title = title,
		self.year = year,
		self.actors = actors

	def __repr__(self):
		return f'Person({self.title},{self.year},{self.actors})'

class MovieSchema(Schema):
	title = fields.Str()
	year = fields.Integer()
	actors = fields.Nested(PersonSchema, many=True)

m1 = Movie('Blade Runner', 1982, [a1, PT('Michael', 'Trovalt', date(1956,5,1)), PT('John', 'Legion', date(1960,7,20))])
print('Movie object: ', MovieSchema().dumps(m1))


print('\n\n-------------------------------------------- Deserializing --------------------------------------------\n')


class PersonSchema(Schema):
	first_name = fields.Str()
	last_name = fields.Str()
	dob = fields.Date()

person_schema = PersonSchema()

# This will do convert the 'Dict' in loads to a 'Marshmallow.data' Dict.
# This will do the initial formatting as per the schema. Like 'dob' will be the datetime.datetime object.
person_schema.load(dict(
					first_name='John',
					last_name='Cleese',
					dob='1989-02-20'
				))

from marshmallow import post_load

class PersonSchema(Schema):
	first_name = fields.Str()
	last_name = fields.Str()
	dob = fields.Date()

	# This will convert the Dict to the 'Person' Class object.
	# But since Marshmallow doesn't know that whenever it has 'data', it will have to return the 'Person' class object.
	# So, we need the decorator to add the functionality where, Marshmallow after 'loading' the 'data', run that 'data'
	# through this function and Return THAT value. We want this value.

	@post_load
	def make_person(self, data):
		return Person(**data)

PersonSchema().load(dict(
					first_name='John',
					last_name='Cleese',
					dob='1989-02-20'
				))
# Output at this point will be:
# >> UnmarshalResult(data=Person(John, Cleese, 1989-2-20), errors={})

class MovieSchema(Schema):
	title = fields.Str()
	year = fields.Integer()
	actors = fields.Nested(PersonSchema, many=True)

	@post_load
	def make_movie(self, data):
		return Movie(**data)

movie_schema = MovieSchema()
person_schema = PersonSchema()
json_data = '''
{
	"actors": [
		{
			"first_name": "John",
			"last_name": "Cleese",
			"dob": "1989-02-20"
		},
		{
			"first_name": "Harrison",
			"last_name": "Ford",
			"dob": "1960-09-01"
		}

	],
	"title": "Blade Runner",
	"year": 1982
}
'''

# This will run the 'make_movie' and return the 'Movie' Object.
# Also, inside the movie_schema, we have instance of 'PersonSchema'. That will run the 'make_person' for every actor
# and return the 'Person' obejct for each actor.
movie = movie_schema.loads(json_data).data
print('Movie title: ', movie.title)
print('Movie Actors: ', movie.actors)


print('\n\n----------------------------------------- Serializing / Deserializing: PyYaml -----------------------------------------\n')
'''
Documentation: https://pyyaml.org/wiki/PyYamlDocumentation

Yaml Format:
	title: Blade Runner
	actors:
		- first_name: John
		  last_name: Cleese
		  dob: 1989-02-20
		- first_name: Harrison
		  last_name: Ford
		  dob: 1960-09-01

NOTE: PyYaml default deserialized output is 'Dictionary' format.
		We can use the Yaml-out Dictionary and feed it into Marshmallow to do stuff that PyYaml can't do.
			Like, get Class Object out (same thign we did for MovieSchema and PersonSchema)

*** We can use PyYaml's Deserializing to get Class Objects. But it uses 'Pickling / Unpickling'. So, need to be careful if we want to
	use that or not (Pickle / Unpickle is not safe as it can execute code pieces while Deserializing.)
'''

import yaml

print('\n----------- Serializing Data -----------\n')

d = {'a': 100, 'b': False, 'c': 10.5, 'd': [1,2,3]}
print('Dict Data: ', d)
# This will print list in Yaml as we have in Python '[ ]'
print('Serialized Data Format 1: ', yaml.dump(d))

# This will print list in Yaml as we have in above example
print('Serialized Data: ', yaml.dump(d, default_flow_style=False))


print('\n----------- Deserializing Data -----------\n')

data = '''
---
title: Blade Runner
actors:
	- first_name: John
	  last_name: Cleese
	  dob: 1989-02-20
	- first_name: Harrison
	  last_name: Ford
	  dob: 1960-09-01

'''
# Deserialize Yaml
d = yaml.load(data)
print('Yaml Data:\n', data)
# Type if 'dict'
print('Type of deserialized data: ', type(d))
print('Deserialized Data:\n', d)
# Now, this Deserialized data has 'dob' in Datetime.date() object as Yaml.load recoganised it as a valid date() format
'''
Output:
{
	title: 'Blade Runner',
	'actors': [{'first_name': 'John',
		'last_name': 'Cleese',
		'dob': datetime.date(1989,2,20)},
	{'first_name': 'Harrison',
	 'last_name': 'Ford',
	 'dob': datetime.date(1960,9,1)}]}
'''
# If there is code piece in Yaml, load() will execute them
# To safely load the Yaml data, there is safe_load(). It will throw error if there is any executable statement in Yaml data.
print('Deserialized Data:\n', yaml.safe_load(d))

# With safe_load() we cannot deserialize any Class Object data out.
# This is where PyYaml comes into picture.

from yaml import YAMLObject, SafeLoader

class Person(YAMLObject):
	yaml_tag = '!Person'

	def __init__(self, name, age):
		self.name = name
		self.age = age

	def __repr__(self):
		return f'Person({self.name},{self.age})'

# Now, yaml.dump(dict(john=Person('John', 34), michael=Person('Michael', 54)))
# will give '!Person' as the type for the Serialized Object
# Output->
# john: !Person {age: 34, name: John}, michael: !Person {age: 54, name: Michael}
print('Serializing with Tag:\n', yaml.dump(dict(john=Person('John', 34), michael=Person('Michael', 54))))

# Now, Deserializing Data
yaml_data = '''
john: !Person
	age: 34
	name: John
michael: !Person
	age: 54
	name: Michael
'''

# load() now will correctly give us 'Person' Class Objects
print('Deserializing Tagged Data:\n', yaml.load(yaml_data))
# Output: {'john': Person(name=John, age=34), 'michael': Person(name=Michael, age=54)}

# But safe_load() still won't know what to do with '!Person'
# print('Deserializing Tagged Data:\n', yaml.safe_load(yaml_data))
# Above will give error.

class Person(YAMLObject):
	yaml_tag = '!Person'
	yaml_loader = SafeLoader

	def __init__(self, name, age):
		self.name = name
		self.age = age

	def __repr__(self):
		return f'Person({self.name},{self.age})'

# Now, safe_loader can be used AS WELL. (load() will work anyways)
print('Deserializing Tagged Data:\n', yaml.safe_load(yaml_data))


print('\n\n----------------------------------------- Serializing / Deserializing: Serpy -----------------------------------------\n')
'''
Documentation: https://serpy.readthedocs.io/en/latest

Schema: Does support Schema while Serializing Objects
Serialization: Extremely Fast Serialization. Output Type = Dict
				We can use 'JSON' or 'YAML' to convert the Serialized Data into 'json' or 'yaml' type
Deserialization: DOES NOT do Deserialization

Usecase: When you only have to Serilize Data and send it to other people.
'''
import serpy
import json, yaml

class Person:
	def __init__(self, name, age):
		self.name = name
		self.age = age

	def __repr__(self):
		return f'Person({self.name},{self.age})'

# We need to tell Serpy how to Serialize 'Person' class objects
class PersonSerializer(serpy.Serilizer):
	name = serpy.StrField()
	age = serpy.IntField()

p1 = Person('Michael Jordan', 50)
print('Person Data: ', p1)
print('Serialized Person Data: ',PersonSerializer(p1).data)
# This will give out a Dictionary.
# Output -> {'name': 'Michael Jordan', 'age': 50}

# For complex Example
class Movie:
	def __init__(self, title, year, actors):
		self.title = title,
		self.year = year,
		self.actors = actors

	def __repr__(self):
		return f'Person({self.title},{self.year},{self.actors})'

class MovieSerializer(serpy.Serilizer):
	title = serpy.StrField()
	year = serpy.IntField()
	actors = PersonSerializer(many=True)

p2 = Person('John Cleese', 39)
m1 = Movie('Blade Runner', 1982, [p1,p2])

print('Movie Data: ', m1)
print('Serialized Movie Data: ',MovieSerializer(m1).data)

print('\nFormatting in JSON and YAML\n')
print('JSON: ', json.dumps(MovieSerializer(m1).data))
print('YAML: ', yaml.dump(MovieSerializer(m1).data))