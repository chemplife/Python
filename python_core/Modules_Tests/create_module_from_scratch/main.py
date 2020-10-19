# To build the path to module1_source and help sys locate it.
import os.path

# To create Module using types.ModuleType
import types

# To load module to sys
import sys

# For search and load module manually
# What will be the name of the module going to be. This doesn't have to match the actual file name, but typically, it is the same
module_name = 'module1'

# Where can we find the file to load the source code up.
module_file = 'module1_source.py'

# Module Path = current path
module_path = '.'

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
exec(code, mod.__dict__)

#######################################################################################

############				 MODULE CREATION IS COMPLETED					###########

#######################################################################################

mod.hello()

# OR

# Now, module1 is not the global directory of this file. But we have module1 created inside this file.
# So, this will work, because we added module1 info in sys

import module1
module1.hello()

# mod and module1 are the same object
print('Is mod and module1 same object?:',mod is module1)