# import datetime
from datetime import datetime
import time

print(datetime(2024,1,1))
print(datetime.now())
# it convert string to datetime object
dt = datetime.strptime("2024/01/01", "%Y/%m/%d")
print(dt)

dt = datetime.fromtimestamp(time.time())
print(dt.year)
print(dt.month)
print(dt.second)
dt = datetime.strptime("2024/01/01", "%Y/%m/%d")

print(dt.strftime("%Y/%m/%d"))
