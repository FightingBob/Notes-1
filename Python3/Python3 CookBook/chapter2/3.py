import re


text = 'Today is 11/27/2012. PyCon starts 3/13/2013.'
datepat = re.compile(r'(\d+)/(\d+)/(\d+)')

print(datepat.sub(r'\3-\2-\1', text))
