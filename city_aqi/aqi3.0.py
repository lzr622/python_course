import pandas as pd

ser_obj = pd.Series(range(10,20))
ser_obj.name = 'hh'
print(ser_obj)
#print(ser_obj.head(5))
#print(ser_obj.tail(4))
print(ser_obj.name)