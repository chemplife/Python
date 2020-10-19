from common.validators import *
import common

print("************ self ************")
for k in dict(globals()).keys():
	print(k)

print("************ Common ************")
for k in common.__dict__.keys():
	print(k)

print("************ Validators ************")
for k in common.validators.__dict__.keys():
	print(k)