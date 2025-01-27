
# calender 
import calendar
yy=2025
mm=1
# print(calendar.calendar(yy))
print(calendar.month(yy,mm))

# Collectins Module
from collections import Counter
list1=[1,2,2,1,2,3,4,21,3,4,5,2,1,4,5,2,1,4,6,3,2,5,6,2,1,45,2,2,4,6,2,3,5,2,3,4]
count=Counter(list1)
print(count)