from datetime import datetime, timedelta

dt1 = datetime(2024, 1, 1) + timedelta(days=1, seconds=1000)
dt2 = datetime.now()

duration = dt2 - dt1

print("days",duration.days)
print("seconds", duration.seconds)
print("total_seconds",duration.total_seconds())
print(duration)