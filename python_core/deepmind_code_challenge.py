import datetime
from datetime import date
f_date = date(2014, 7, 2)
l_date = date(2014, 7, 11)
delta = l_date - f_date
print(delta.days)
print(type(delta.days))

month = '2019-01'
billing_month_in_list = month.split("-")
first_date_of_month = datetime.date(int(billing_month_in_list[0]),int(billing_month_in_list[1]), 1)

d = {
    'id': 1,
    'name': 'Employee #1',
    'customer_id': 1,

    # when this user started
    'activated_on': datetime.date(2018, 11, 4),

    # last day to bill for user
    # should bill up to and including this date
    # since user had some access on this date
    'deactivated_on': datetime.date(2019, 1, 10)
  }
print(d.get('activated_on'))

billing_month_active_users=0

if (d.get('activated_on')<=first_date_of_month) and (d.get('deactived_on') is None or not(d.get('deactived_on') <=first_date_of_month)):
	billing_month_active_users+=1

print(billing_month_active_users)