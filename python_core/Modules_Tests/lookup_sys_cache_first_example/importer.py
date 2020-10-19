import os.path
import types
import sys

print('Running Importer.py')

def import_(module_name, module_file, module_path):

	# Check for the module in sys cache first before creating the module
	# If it is there, return it
	if module_name in sys.modules:
		return sys.modules[module_name]

	# If module is not in sys cache, create 1 from scratch, like earlier.
	# Build up the path
	module_rel_file_path = os.path.join(module_path, module_file)
	module_abs_file_path = os.path.abspath(module_rel_file_path)

	# Read the source code from file
	with open(module_rel_file_path, 'r') as code_file:
		source_code = code_file.read()

	# create a module object
	mod = types.ModuleType(module_name)

	# Where does the module code come from?
	mod.__file__ = module_abs_file_path

	# set a reference in sys module, which is a dictionary
	# at this point, module 'mod' has nothing
	sys.modules[module_name] = mod

	# To complete the module setup, 1st we have to compile the source code
	# Filename is just for metadata, it is not going to go back and read it.
	# mode = 'exec' for compiling multiline code.
	code = compile(source_code, filename=module_abs_file_path, mode='exec')

	# execute the compiled python binary code file
	# 2nd argument is the dictionary to be used to create the namespace (where global stuff goes)
	# So, when we do 'import' for this module, it puts the module in global namespace that will point
	# the compiler to the compiled object in memory.
	exec(code, mod.__dict__)

	#######################################################################################

	############				 MODULE CREATION IS COMPLETED					###########

	#######################################################################################

	# Now, we will return the module from sys cache

	return sys.modules[module_name]

"""
Importer can read the source code from any type of file format, including zip, egg, etc.
It works on basic principle
	1. Finders - Responsible to find/search the module that we want to import. (compiler ask different finders for the module.)
				 When a finder says 'I know this module' and provides the location, it alse tells which loader to use for loading
				 	the module.
				 Finder returns a 'spec' for the module.
				 module_name.__spec__ -> ModuleSpec(name='module name', loader='<loader to use>', origin='<path of the module>')

				 sys.meta_path -> Returns all the Finder Objects available to Python as List (depends on the Python Package).
				 	- If our module directory path is not in here, we need to add it.
				 		1. Manually -> (sys.meta_path.append(ext_module_path))
				 		2. Site (.pth) -> Create a file that contains all the paths that we want to add.
				 						  Look up python documentation on this.

	2. Loaders - Python compiler tells the loader that here is the module path, please load it. This finishs the task.
				 Loading means: Reading Source_code + adding module info in sys.modules[] + compile + execute

	3. Finder + Loader == Importer - they can do both the tasks done by Finders and Loaders

#########################################################################################
*** It we make our own Finders and Loaders, we need to add them in the sys.meta_path. ***
Eg: Finders and Loaders to load modules from a DB or API response. **********************
#########################################################################################
"""

from importlib import util
# To get spec of a module without loading it
print('Spec of decimal module without loading it:', util.find_spec('decimal'))