'''
Serializing/Deserializing Objects
Useful when dealing with persisting data or for Transmiting Data.
	-> Data that we want to 'save' somewhere so that is can 'loaded' at later time.
	-> Even after the program is terminated.
	-> Transmit the data outside of the app.

It can be applied to any object:
	-> Persistent Representation of object:			Serializing
	-> Reconstruct Object from Serialized Data: 	Deserializing

Serializing/Deserializing together called as 'Data Marshalling'.

Pickling and Unpickling: Serialize/Deserialize Python objects using Binary representation through Built-in mechanisms

	-> Pickling: Is done for Mainly Dictionary but can be done on other Objects.
	-> Unpickling: Can potentially EXECUTE Code.
				-> So, we should only be unpickling the data that we trust.

	How?
		Pickling:
			->	import pickle
				dump			-> pickle to file
				load 			-> unpickle from file
				dumps			-> return a (string) picked representation (Doesn't store in any file.)
				loads			-> It takes a pickled string to unpickle it.

'''

import pickle

a = [1,2,3,4]
print('Data: ',a)
ser = pickle.dumps(a)
print('Serialized output: ',ser)
deser = pickle.loads(ser)
print('Deserialized Data: ',deser)