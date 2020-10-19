import decimal
from decimal import Decimal

# getcontext() gives current 'context' object of decimal class.
# in this case, the global context
ct = decimal.getcontext()
print('Global Type:', type(ct))
print('Global:',ct)

ct.prec = 12
ct.rounding = decimal.ROUND_HALF_UP
print('Global Changed:',ct)

i = Decimal('0.12745')
print('i:',round(i,2))
# localcontext() gives 'ContextManager' type object
print('Local:',decimal.localcontext())
print('Local type:', type(decimal.localcontext()))

# localcontext() along with 'with', gives a 'context' type object
with decimal.localcontext() as ctx:
	print('with local type:',type(ctx))
	print('with local:',ctx)

	ctx.prec = 6
	ctx.rounding = decimal.ROUND_HALF_DOWN

	print('with local changed:',ctx)

	# this gives the current context, in this case the local context
	print('Conext:', decimal.getcontext())
	print(id(ctx) == id(decimal.getcontext()))
