import decimal
from decimal import Decimal

#prec won't effect a, b (storage of value)
a = Decimal('0.1234')
b = Decimal('0.3456')

#prec will effect the operation result
print('Global prec:',decimal.getcontext().prec)
print('a:{0}, b:{1}'.format(a,b))
print(a+b)

with decimal.localcontext() as ctx:
	ctx.prec = 2
	print('local prec:',ctx.prec)
	print(f'a:{a}, b:{b}')
	print(a+b)

#Tuple and float for decimal.
c = Decimal(0.1234)
print('Float:',c)

# 'Tuple' and 'string' are more accurate than 'float' values
d = Decimal((0,(1,2,3,4),-4))
e = Decimal((1,(1,2,3,4),-4))
print('+ Tuple:',d)
print('- Tuple:',e)

print(c==a)
print(d==a)