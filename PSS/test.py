from datetime import datetime, timedelta, date, time
from random import getrandbits

print(getrandbits(1))
now = datetime.now()
now = now.replace(minute=0, second=0, microsecond=0)
start_time = datetime(now.year, now.month, now.day - 1, now.hour, 0, 0)
hour_count = int((now - start_time).total_seconds() / 3600)
print(hour_count)
print(now.year)
test_day = date(2019,1,1)
print(test_day)
for consid_datetime in (start_time + timedelta(hours=n) for n in range(hour_count + 1)):
    print(consid_datetime)

print(now.date())
print(now.time())

