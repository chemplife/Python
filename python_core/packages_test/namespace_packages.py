"""
Any package that does not have __init__.py file is namespace package.


utils/								-> Doesn't have __init__.py (NAMESPACE Package)

	validators/						-> Doesn't have __init__.py (NAMESPACE Package)
		boolean.py					-> Module
		numeric.py					-> Module

		json/						-> Does have __init__.py (Regular Package)
			__init__.py
			serializer.py			-> Module
			validator.py			-> Module


				Regular Package 			|				NameSpace Package
											|
type -> Module								|	type -> Module
											|
Has code associate to the module, 			|	Have no code associated to this module
	__init__.py file						|	No __init__.py file
											|
__file__ -> has package __init__			|	__file__ -> Not Set
											|
path ->	use relative paths for import or	|	path -> Dynamically computed when program compiles.
		in case of parent directory			|			It is ok if parent directory name changes.
		name-change, things will break		|
											|
Single package lives in a single directory	|	single package can live in multiple (non-nested) directories
											|	even parts of namespace package can be in zip file.


app/
	utils/					-> NameSpace Package
		validators/			-> NameSpace Package
			boolean.py
	common/					-> Regular Package
		__init__.py
		validators/			-> NameSpace Package
			boolean.py


			  				NameSpace Package 							Regular Package
								utils										common

type		----				Module 										Module
__name__	----				utils 										common
__repr__()	----		<module utils (namespace)>				<module common from '../app/common'
__path__	----		_Namespace([../app/utils])						['../app/common']
__file__	----				not Set 							../app/common/__init__.py
__package__	----				utils										common

-> validators---			utils.validators							common.validators




"""