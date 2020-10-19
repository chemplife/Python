class Stock:
	def __init__(self, symbol, date, open_, high, low, close, volume):
		self.symbol = symbol
		self.date = date
		self.open = open_
		self.high = high
		self.low = low
		self.close = close
		self.volume = volume


class Trade:
	def __init__(self, symbol, timestamp, order, price, volume, commission):
		self.symbol = symbol
		self.timestamp = timestamp
		self.order = order
		self.price = price
		self.volume = volume
		self.commission = commission


'''
Exercise-1 : Give above classes, write a custom JSONEncoder, to serialize the dictionaries that contain instances of these classes.
			We also have deserialize the data so, we need some way to indicate the object type in our serialization.

Exercise-2: Deserialize the instance we serialized in Exercise-1
Exercise-3: Do, serialization and Deserialization using 'Marshmallow'
'''

# adding new method in 'Stock' and 'Trade' classes
def as_dict_stock(self):
	return dict(symbol=self.symbol,
				date=self.date,
				open=self.open,
				high=self.high,
				low = self.low,
				close=self.close,
				volume=self.volume
				)
Stock.as_dict = as_dict_stock

def as_dict_trade(self):
	return dict(symbol=self.symbol,
				timestamp=self.timestamp,
				order=self.order,
				price=self.price,
				volume=self.volume,
				commission=self.commission
				)
Trade.as_dict = as_dict_trade

# Sample data
from datetime import date, datetime
from decimal import Decimal

activity = {
	"quotes": [
		Stock('TSLA', date(2018, 11, 22), Decimal('338.19'), Decimal('338.64'), Decimal('337.60'), Decimal('338.19'), 365_307),
		Stock('AAPL', date(2018, 11, 22), Decimal('176.66'), Decimal('177.25'), Decimal('176.64'), Decimal('176.78'), 3_699_184),
		Stock('MSFT', date(2018, 11, 22), Decimal('103.25'), Decimal('103.48'), Decimal('103.07'), Decimal('103.11'), 4_493_689),
	],
	"trades": [
		Trade('TSLA', datetime(2018, 11, 22, 10, 5, 12), 'buy', Decimal('338.25'), 100, Decimal('9.99')),
		Trade('AAPL', datetime(2018, 11, 22, 10, 30, 5), 'sell', Decimal('177.01'), 20, Decimal('9.99'))
	]
}


#### Exercise-1
'''
{
	"object": 'Stock' or 'Trade',
	rest_of_the_Data...
}
This is because we need to deserialize the data as well so we need to know the what type is the data..
'''
from json import JSONEncoder, dumps

class CustomEncoder(JSONEncoder):
	def default(self, obj):
		if isinstance(obj, Stock) or isinstance(obj, Trade):
			result = obj.as_dict()
			result['object'] = obj.__class__.__name__
			return result

		elif isinstance(obj, datetime):
			return obj.strftime('%Y-%m-%dT%H:%M:%S')

		elif isinstance(obj, date):
			return obj.strftime('%Y-%m-%d')

		elif isinstance(obj, Decimal):
			return str(obj)

		else:
			super().default(obj)

encode = dumps(activity, cls=CustomEncoder, indent=2)
print(encode)

print('-----------------------------------------------------------------------')
#### Exercise-2

def decode_stock(d):
	s = Stock(d['symbol'],
			  datetime.strptime(d['date'], '%Y-%m-%d').date(),
			  Decimal(d['open']),
			  Decimal(d['high']),
			  Decimal(d['low']),
			  Decimal(d['close']),
			  int(d['volume'])
		)
	return s

def decode_trade(d):
	t = Trade(d['symbol'],
			  datetime.strptime(d['timestamp'], '%Y-%m-%dT%H:%M:%S'),
			  d['order'],
			  Decimal(d['price']),
			  int(d['volume']),
			  Decimal(d['commission'])
		)
	return t

def decode_financials(d):
	object_type = d.get('object', None)
	if object_type == 'Stock':
		return decode_stock(d)
	elif object_type == 'Trade':
		return decode_trade(d)
	return d


from json import JSONDecoder, loads


class CustomDecoder(JSONDecoder):
	def decode(self, arg):
		data = loads(arg)
		return self.parse_financials(data)

	def parse_financials(self, obj):
		if isinstance(obj, dict):
			obj = decode_financials(obj)
			if isinstance(obj, dict):
				for key, value in obj.items():
					obj[key] = self.parse_financials(value)
		elif isinstance(obj, list):
			for index, item in enumerate(obj):
				obj[index] = self.parse_financials(item)
		return obj

decode = loads(encode, cls=CustomDecoder)
print(decode)

# Add Equality Check for both 'Stock' and 'Trade' classes
def equality_stock(self, other):
	return isinstance(other, Stock) and self.as_dict() == other.as_dict()
Stock.__eq__ = equality_stock

def equality_trade(self, other):
	return isinstance(other, Trade) and self.as_dict() == other.as_dict()
Trade.__eq__ = equality_trade

print('\nIs Decoded is same as Actual? ', decode == activity)

print('-----------------------------------------------------------------------')

#### Exercise-3
from marshmallow import Schema, fields, post_load
from pprint import pprint

# Decimal(as_string=True) -> Will help the marshmallow serializer to serialize the data into JSON..
class StockSchema(Schema):
	symbol = fields.Str()
	date = fields.Date()
	open_ = fields.Decimal(as_string=True)
	high = fields.Decimal(as_string=True)
	low = fields.Decimal(as_string=True)
	close = fields.Decimal(as_string=True)
	volume = fields.Integer()

	# This will create the 'Trade' object from the 'data' dict.
	@post_load
	def make_stock(self, data):
		data['open_'] = data.pop('open')
		return Stock(**data)


class TradeSchema(Schema):
	symbol = fields.Str()
	timestamp = fields.DateTime()
	order = fields.Str()
	price = fields.Decimal(as_string=True)
	volume = fields.Integer()
	commission = fields.Decimal(as_string=True)

	# This will create the 'Trade' object from the 'data' dict.
	@post_load
	def make_trade(self, data):
		return Trade(**data)


class ActivitySchema(Schema):
	quotes = fields.Nested(StockSchema, many=True)
	trades = fields.Nested(TradeSchema, many=True)

print('----- Encoded -----')
#Serialize
encode_m = ActivitySchema().dumps(activity, indent=2).data
print(encode_m)

print('----- Decoded -----')
# Deserialize
decode_m = ActivitySchema().loads(encode_m).data
pprint(decode_m)