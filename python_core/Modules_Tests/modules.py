"""
When Python sees a module,
1. It checks if the module is already loaded in sys.modules cache (dictionary). If it is, it will use that reference.
2. If not, python will create a new module object (types.ModuleType)
3. Load the source code from file (it will look for the file path in sys.path, or user specified path)
4. add an entry to sys.module dictionary
5. compiles and executes the source_code

When a module is imported, it is EXECUTED at that time.
"""

print('--------------------Built-In Modules----------------------')
import sys
print(sys.__dict__)
print(sys)

print('\n--------------------Create Module----------------------')
# similarly, math, fraction, collections, are some examples of modules
# we can create our own module.
from types import ModuleType
from collections import namedtuple

# This creates the module, which means the namespace dictionary (mymodule.__dict__) is created at this point. It is empty though
mymodule = ModuleType('test_module_name', 'test_module optional doc_string')
print('Is mymodule a ModuleType?: ',isinstance(mymodule, ModuleType))

mymodule.string = 'I added this string to module'
mymodule.hello = lambda: 'Hello! from my module function.'
print('Check mymodule dictionary: ',mymodule.__dict__)
print('mymodule function call:', mymodule.hello())

mymodule.Point = namedtuple('Point', 'x y')
pt = mymodule.Point(0,0)
pt_2 = mymodule.Point(1,1)

print('mymodule directory: ', dir(mymodule))
PT = getattr(mymodule, 'Point')
PT(20,30)
print('PT:', PT)
print(PT is mymodule.__dict__['Point'])

"""
When we do
import sys
import collections
import fraction etc

How does python know where to find them?

If we do
import mod_name

we cannot import a module if it sitting in a variable name
We wrote the importer.py to implement what 'import' does,
but python provides 'importlib.import_module(mod_name)' to do the same and more.

Now, this will just put the 'mod_name' in sys.modules[], but we don't have it in our program namespace (in globls() dict)
	- But if we use regular 'import', compiler adds the reference of the module in global namespace,
		- This module in global() points to the same reference stored in sys.modules[]
	- If not regular 'import' we need to add this module in global() namespace.
		- Check (Learning/Test Codes/Modules_Tests/lookup_sys_cache_first_example/main.py) for example

***************************
when we do
from math import sqrt
	- It still loads the whole math module in sys.modules[]
	- in program's global namespace, we only see 'sqrt' and not math.
	- so, if someone says doing this is more efficient, IT IS NOT. WE STILL LOAD THE WHOLE MODULE.
	- Yes, it is 1 less lookup to do 'math.sqrt' than looking up 'sqrt', but dict_lookups are exremely fast
		and there not much time we gain doing this.
		(if you are doing this like billion times in your code, then it surely makes some difference.
		Anything less than upto 10-100 million, time gain is close to '0')

when we do
from math import *
from cmath import *
	- we override the common functions between the 2 modules like sqrt, sin, etc. in the global namespace
	- Best is to
		- import math, cmath
		- or
		- from math import sin as r_sin AND from cmath import sin as c_sin

***************************

============================== Reloading Modules ==============================

What will happen if module is imported in our file and we make a change in the module source_code?
	- Since module reference exist in sys.modules[], the compiler is not going to load it again
		(unless the whole program is restarting)
	- So, anywhere the module is used, it is going to use the older version of the module
	-Fix:
		- del sys.modules['module_name'] (put this in the code where we delete the reference of the module from sys.modules[]
											so that next time, it will get loaded to sys.modules[] again and use the updated code)
		- importlib.reload('module_name') (it will just reload the module without even changing the memory address of the reference.
											Anywhere in code if this module is being used, they don't need to worry about anything.)

	[2nd way is much better way to use.]

	**** Still, if someone did
		from module_name import function_name

		importlib.reload('module_name')
			- This will reload the module_name in sys.modules[] and load the updates
			- But the global namespace never had module_name. So, function_name will still point to the older version.

	**** that is why we shouldn't do 'reload' in PROD code.

"""