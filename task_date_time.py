

from datetime import datetime, timedelta

#Напечатайте в консоль даты: вчера, сегодня, месяц назад

dt_now = datetime.now()
dt_yesterday = dt_now - timedelta(days=1)
month_ago = int(dt_now.strftime('%m')) - 1

print('Yesterday: {}'.format(dt_yesterday.date()))
print('Today: {}'.format(dt_now.date()))
print(dt_now.strftime('One month ago: %Y-{}-%d').format(month_ago))

#Превратите строку "01/01/17 12:10:03.234567" в объект datetime

date_string = "01/01/17 12:10:03.234567"
date_dt = datetime.strptime(date_string,'%d/%m/%y %H:%M:%S.%f')
print(date_dt)
