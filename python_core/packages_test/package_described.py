"""
The directory this file is in, is now a python package.

Package: It is a MODULE that has additional functionalities.
		 - It can have more packages inside it
		 - It can have module inside it.

To make any directory a package recoganisable by python compiler,
	- There needs to be a __init__.py file in it.

Eg:
app/
	pack1/
		__init__.py
		module1.py
		module2.py

Now,
import pack1
			-> pack1 code is in __init__.py file
			-> code is loaded and execute in sys.modules['pack1']:			JUST LIKE A MODULE
			-> 'pack1' will be added to the global namespace of the file:	JUST LIKE A MODULE

Package and Module, difference:
	- __path__:
		- module_name.__path__: either EMPTY or MISSING
		- package_name.__path__: contains ABSOLUTE PATH to the Package.
	- __file__:
		- module_name.__file__: ABSOLUTE path to file that contains source_code of the Module.
		- package_name.__file__: ABSOLUTE path to __init__.py file
	- __package__:
		- module_name.__package__: package the module_code is located in. If Module is in application root, this is empty.
		- package_name.__package__: contains 'package_name' (it's own name.)
			(In case of nested packaged, the inner package_name is: pack1.pack_inner)


app/
	module_root.py

	pack1/
		__init__.py
		module1.py
		module2.py

		pack_inner/
				__init__.py
				module1_inner.py
				module2_inner.py

module_root.py
	import pack1.pack_inner.module1_inner.py

	- Sequence of loading
		- Load pack1 			and cache it in sys.modules['pack1']
		- Load pack_inner 		and cache it in sys.modules['pack_inner']
		- Load module1_inner.py and cache it in sys.modules['module1_inner']
		- global namespace will have 'pack1' in it.		-> global()['pack1'] / module_root.__dict__['pack1']

**** While loading pack1 and pack_inner, they execute __init__.py files and load any dependent modules as well.

############################################################################################################################
############################################################################################################################

So, it can be EXTREMELY USEFUL
If we do
	- import pack1 or import pack1.pack_inner
		(By default- The modules in these packages are NOT going to load in sys.modules[].
		 So, we cannot access them.)
		- pack1.module1a.value -> will NOT work (Until we 'import pack1.module1a') -> or any other module in these package.

	- So, to access all the modules in a package just by import package_name
		- import module_name -> inside __init__.py file of the package
								(Because __init__.py file gets executed when the package is imported
								 and it will import all the imports of __init__.py file.)

############################################################################################################################
############################################################################################################################
"""
