"""A date in Python is not a data type of its own, but we can import a module named datetime to work with dates as date objects."""

import datetime as dt

x = dt.datetime.now()
print(x)
print(x.year)
print(x.strftime("%A"))
print(x.strftime("%B"))
x1 = dt.datetime(2020, 5, 17)
print(x1)