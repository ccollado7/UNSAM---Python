# -*- coding: utf-8 -*-
"""
Created on Mon Sep 28 13:46:00 2020

@author: User
"""

#%%
#Fecha y hora actuales

import datetime

fecha_hora = datetime.datetime.now()
print(fecha_hora)

#%%
#Fecha actual

fecha = datetime.date.today()
print(fecha)

#%%
#Objetos tipo fecha

d = datetime.date(2019,4,13)
print(d)

from datetime import datetime
e = date(2019,4,13)
print(e)

#%%
#Timestamp

from datetime import date

timestamp = date.fromtimestamp(1326244364)
print('Fecha =',timestamp)


hoy = date.today()

print('Año actual:', hoy.year)
print('Mes actual:', hoy.month)
print('Dia actual:', hoy.day)
print('Dia de la semana:', hoy.weekday())


#%%

from datetime import time

a = time()       # time(hour = 0, minute = 0, second = 0)
print('a =', a)

b = time(11, 34, 56)
print('b =', b)

c = time(hour = 11, minute = 34, second = 56)
print('c =', c)

d = time(11, 34, 56, 234566)  # time(hour, minute, second, microsecond)
print('d =', d)

#%%

from datetime import time

a = time(11, 34, 56)

print('hour =', a.hour)
print('minute =', a.minute)
print('second =', a.second)
print('microsecond =', a.microsecond)

#%%

from datetime import datetime

a = datetime(2020,4,21)
print(a)

b = datetime(2021, 4, 21, 6, 53, 31, 342260)
print(b)

#%%
from datetime import datetime

a = datetime(2021, 4, 21, 6, 53, 31, 342260)
print('año =', a.year)
print('mes =', a.month)
print('día =', a.day)
print('hora =', a.hour)
print('minuto =', a.minute)
print('timestamp =', a.timestamp())

#%%
#timedelta

from datetime import datetime, date

t1 = date(year = 2021, month = 4, day = 21)
t2 = date(year = 2020, month = 8, day = 23)
t3 = t1 - t2
print(t3)


t4 = datetime(year = 2020, month = 7, day = 12, hour = 7, minute = 9, second = 33)
t5 = datetime(year = 2021, month = 6, day = 10, hour = 5, minute = 55, second = 13)
t6 = t4 - t5
print(t6)

#%%

from datetime import timedelta

t1 = timedelta(weeks = 1, days = 2, hours = 1, seconds = 33)
t2 = timedelta(days = 6, hours = 11, minutes = 4, seconds = 54)
t3 = t1 - t2

print('t3 =', t3)

#%%

from datetime import timedelta

t1 = timedelta(seconds = 21)
t2 = timedelta(seconds = 55)
t3 = t1 - t2

print(t3)

#%%

from datetime import timedelta

t = timedelta(days = 1, hours = 2, seconds = 30, microseconds = 100000)
print('segundos totales =', t.total_seconds())


#%%

from datetime import datetime

cadena_con_fecha= '21 September, 2021'
print('date_string =', cadena_con_fecha)


date_object = datetime.strptime(cadena_con_fecha, '%d %B, %Y')
print('date_object =', date_object)

cadena_con_fecha_1 = '02/04/1985'
date_object_1 = datetime.strptime(cadena_con_fecha_1, '%m/%d/%Y')
print('date_object =', date_object_1)