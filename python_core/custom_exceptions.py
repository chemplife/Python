'''
Custom Exceptions needs to be inherited from any of the subclasses of class 'BaseException'
-> Most commonly, we will be using class 'Exception' or any of its subclasses
'''

class TimeoutError(Exception):
	'''Timeout Exception Occurred'''

try:
	raise TimeoutError('Timeout Exception Occurred')
except TimeoutError as ex:
	print(repr(ex))

print('\n')

import sys

try:
	raise TimeoutError('Timeout Exception Occurred')
except:
	ex_type, ex, tb = sys.exc_info()
	print(f'Bare Exception info:\n\tType:\t   {ex_type}\n\tException: {ex}\n\tTraceback: {tb}')

print('\n')

try:
	raise TimeoutError('Timeout Exception Occurred')
except TimeoutError as ex:
	print(ex.args, ':', ex.__traceback__)

print('\n\n---------------------- Usecase 1: WebScrapper Exception Class ----------------------\n')
# Any Exception related to 'WebScrapping' will use our custom 'WebScrapper Exception Class'

class WebSrcapperException(Exception):
	'''Base Exception Class for WebScrapper'''

class HTTPException(WebSrcapperException):
	'''General HTTP Exception for WebScrapper'''

class InvalidUrlException(HTTPException):
	'''Indicates that the URL is invalid (dns lookup failed..)'''

class TimeoutException(HTTPException):
	'''Indicates a general Timeout Txception in HTTP connectivity'''

class PingTimeoutException(TimeoutException):
	'''Ping Timeout'''

class LoadTimeoutException(TimeoutException):
	'''Page Load Timeout'''

class ParserException(WebSrcapperException):
	'''General Page Parseing Exception'''

try:
	raise LoadTimeoutException('Page www.google.com did not load in time..')
# We can use any of
# 1. WebSrcapperException,
# 2. HTTPException
# 3. TimeoutException
# 4. LoadTimeoutException
# Result will be the same..
except WebSrcapperException as ex:
	print('Exception: ', repr(ex))

print('\n\n---------------------- Usecase 2: API Exception Class ----------------------\n')
# Any Exception related to 'WebScrapping' will use our custom 'WebScrapper Exception Class'

class APIException(Exception):
	'''Base Exception Class for API'''

class ApplicationException(APIException):
	'''Indicates an Application Error (not user caused)- 5xx HTTP type errors'''

class DBException(ApplicationException):
	'''General Database Exception'''

class DBConnectionError(DBException):
	'''Indicates an Error Connecting to Database'''

class ClientException(APIException):
	'''Indicates Exception caused by User- Not internal Error'''

class NotFoundError(ClientException):
	'''Indicates Resource was Not Found'''

class NotAuthorizedError(ClientException):
	'''User is not Authorized to perform requested action on resource'''

# Our Application Class
class Account:
	def __init__(self, account_id, account_type):
		self.account_id = account_id
		self.account_type = account_type

def lookup_account_by_id(account_id):
	if not isinstance(account_id, int) or account_id <= 0:
		raise ClientException(f'Account Number {account_id} is invalid')

	if account_id < 100:
		raise DBConnectionError('Permanent Failure Connecting to Database')
	elif account_id < 200:
		raise NotAuthorizedError('User does not have permission to read this account.')
	elif account_id < 300:
		raise NotFoundError('Account not found.')
	else:
		return Account(account_id, 'Savings')


from http import HTTPStatus

def get_account(account_id):
	try:
		account = lookup_account_by_id(account_id)
	except ApplicationException as ex:
		return HTTPStatus.INTERNAL_SERVER_ERROR, str(ex)
	except NotFoundError as ex:
		return HTTPStatus.NOT_FOUND, 'The Account {} does not exist'.format(account_id)
	except NotAuthorizedError as ex:
		return HTTPStatus.UNAUTHORIZED, 'You do not have proper authorization.'
	except ClientException as ex:
		return HTTPStatus.BAD_REQUEST, str(ex)
	else:
		return HTTPStatus.OK, {"id": account.account_id, "type": account.account_type}

print(get_account('abc'))
print(get_account(150))
print(get_account(250))
print(get_account(350))


# Now, different Developer would be showing different HTTPStatuses for each of these exceptions..
# IT is good idea to make the Messages to user more consistent and the Application Error Logs, more specific to errors.
print('\n\n---------------------- Usecase 2: API Exception Class- Refined ----------------------\n')


import json
from datetime import datetime

class APIException(Exception):
	'''Base Exception Class for API'''

	# default HTTP Status
	http_status = HTTPStatus.INTERNAL_SERVER_ERROR
	internal_err_msg = 'API Exception Occurred'
	user_err_msg = 'We are Sorry! An unexpected error occurred on our end.'

	# Overriding the BaseException __init__()
	def __init__(self, *args, user_err_msg=None):
		if args:
			self.internal_err_msg = args[0]
			super().__init__(*args)
		else:
			super().__init__(self.internal_err_msg)

		if user_err_msg is not None:
			self.user_err_msg = user_err_msg

	# API needs to return a JSON response:
	def to_json(self):
		err_object = {"status": self.http_status, "message": self.user_err_msg}
		return json.dumps(err_object)

	# Log the Exception
	def log_exception(self):
		exception = {
			"type": type(self).__name__,
			"http_status": self.http_status,
			"message": self.args[0] if self.args else self.internal_err_msg,
			"args": self.args[1:] if (self.args and len(self.args)>1) else None
		}
		print(f'EXCEPTION: {datetime.utcnow().isoformat()}: {exception}')


class ApplicationException(APIException):
	'''Indicates an Application Error (not user caused)- 5xx HTTP type errors'''
	http_status = HTTPStatus.INTERNAL_SERVER_ERROR
	internal_err_msg = 'Generic Server Side Exception'
	user_err_msg = 'We are Sorry! An unexpected error occurred on our end.'

class DBException(ApplicationException):
	'''General Database Exception'''
	http_status = HTTPStatus.INTERNAL_SERVER_ERROR
	internal_err_msg = 'Database Exception'
	user_err_msg = 'We are Sorry! An unexpected error occurred on our end.'

class DBConnectionError(DBException):
	'''Indicates an Error Connecting to Database'''
	http_status = HTTPStatus.INTERNAL_SERVER_ERROR
	internal_err_msg = 'Database Connection Exception'
	user_err_msg = 'We are Sorry! An unexpected error occurred on our end.'

class ClientException(APIException):
	'''Indicates Exception caused by User- Not internal Error'''
	http_status = HTTPStatus.BAD_REQUEST
	internal_err_msg = 'Client Submitted Bad Request'
	user_err_msg = 'A bad request was received.'

class NotFoundError(ClientException):
	'''Indicates Resource was Not Found'''
	http_status = HTTPStatus.NOT_FOUND
	internal_err_msg = 'Resource Not Found'
	user_err_msg = 'Request Resource Not Found.'

class NotAuthorizedError(ClientException):
	'''User is not Authorized to perform requested action on resource'''
	http_status = HTTPStatus.UNAUTHORIZED
	internal_err_msg = 'Client Not Authorized to Perform Operation'
	user_err_msg = 'You are not authorized to perform this operation.'


def lookup_account_by_id(account_id):
	if not isinstance(account_id, int) or account_id <= 0:
		raise ClientException(f'Account Number {account_id} is invalid,',
							  f'account_id = {account_id}',
							  'type error - account number not an integer.')

	if account_id < 100:
		raise DBConnectionError('Permanent Failure Connecting to Database,', 'db = db01')
	elif account_id < 200:
		raise NotAuthorizedError('User does not have permission to read this account.', f'account_id= {account_id}')
	elif account_id < 300:
		raise NotFoundError('Account not found.', f'account_id= {account_id}')
	else:
		return Account(account_id, 'Savings')

def get_account(account_id):
	try:
		account = lookup_account_by_id(account_id)
	except APIException as ex:
		ex.log_exception()
		return ex.to_json()
	else:
		return HTTPStatus.OK, {"id": account.account_id, "type": account.account_type}

print(get_account('abc'))
print(get_account(150))
print(get_account(250))
print(get_account(350))


print('\n\n---------------------- Exception Class Inherited from Mutliple Classes (Multiple Inheritance) ----------------------\n')

class AppExceptions(Exception):
	'''Generic Application Exception'''

# An integer error in 'age' can happen both due to 'Negative-Value' or other 'ValueErrors'..
class NegativeIntegerError(AppExceptions, ValueError):
	'''Used to indicate when the error is occured due to negative value'''

ex = NegativeIntegerError()
print('NegativeIntegerError is an instance of AppExceptions?:', isinstance(ex, AppExceptions))
print('NegativeIntegerError is an instance of ValueError?:', isinstance(ex, ValueError))

def set_age(age):
	if age < 0:
		raise NegativeIntegerError('Negative Age Entered..')

try:
	set_age(-10)
except ValueError as exc:
	print('Exception happened: ', repr(exc))
