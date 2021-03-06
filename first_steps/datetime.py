# -*- coding: utf-8 -*-
"""
Created on Sat Oct 12 16:55:03 2019 -18:23:06 2019

@author: EconBeast
Topic: handling dates and times!
Description: I think one of the more underrated tasks is how to handle dates.
Given the variety of formats, I'll try my best to show you how to handle dates
for better data readability.
"""
# packages to import, plus date and time package

import pandas as pd
import numpy as np
from datetime import datetime
from datetime import timedelta
# Working with dates is particularly important when it comes to working with
# panel data, time series data, financial data, all of course not independent

Today = datetime.now()  # will show today's data

# These are also possible
Today.year
Today.month
Today.day
Today.minute

# To capture the difference between dates, you can subtract.
# To illustrate, I used my birthday. I was born 9039 days ago
# If you are using spyder, check the object created. It's called a
# 'timedelta'. You can extract days from it.
time_elapsed = datetime(2019, 10, 12) - datetime(1995, 1, 12)
time_elapsed.days

# Lets use the function timedelta. timedelta has several arguments, from day
# to microseconds.It's useful when you want to add time to a date, but not a
# long run solution.

yesterday = datetime(2019, 10, 11)
Today = yesterday + timedelta(1)

# The next significant component would be parsing data. Typically, you have
# this dataset where the dates and times are strings. We are going to use
from dateutil.parser import parse

# Parse can read any date format ever imagined.
# It takes a string as an argument and breaks it down in the appropriate units.
Today = str(Today)
Today1 = parse(Today)  # converts the string to a datetime

date_format1 = parse('21, 06, 1995', dayfirst=True)
date_format2 = parse('21-06-1995', dayfirst=True)

# It can even parse when it doesn't make sense.
date_format3 = parse('21-06-1995', dayfirst=False)
date_format3.day

date_format4 = parse('6/4/2001', dayfirst=False)
date_format5 = parse('June 4th, 2009 10:45 pm')
# As you noticed, parse is powerful.
# The thing with parse though is that it has to return a year, month, day, so
date_format6 = parse('06-1995')
# will also include the day, hour, min and sec since it is a datetime object

# But, you can use .strptime. See your string and format it how you want it.
# This will return a datetime object. The format code can be googled
date_format7 = datetime.strptime('06-1995', '%m-%Y')


# When handling a column of dates or times, you can use:
column_of_dates = [
    '06-03-2014',
    '06-04-14'
]
dataframe_dates = pd.to_datetime(column_of_dates)   # will read as month first
dataframe_dates2 = pd.to_datetime(column_of_dates, dayfirst=True)  # day first

# Also you can use datetime to put columns (series) together if year, month,
# day are separate
dataframe = pd.DataFrame({
    'year': [1995, 1996, 1997],
    'month': [2, 3, 4],
    'day': [27, 17, 16]}
)
date_index = pd.to_datetime(dataframe)
# Resulting time series df usinf index
ts = pd.Series(np.random.randn(3), index=date_index)

# date_range is another powerful method. By setting a starting date,
# you can create an index for x periods starting at y
index = pd.date_range(start='01/01/2000', periods=365, freq='d')  # d= daily
