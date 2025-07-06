

import datetime

# datetime.date
# datetime.time
# datetime.datetime
# datetime.timedelta


nw = datetime.datetime.now()
print("current date is", nw)

nw1 = datetime.date.today()
print("current date is", nw1)

specific_date = datetime.date(2025, 2, 17)
print(specific_date)

specific_time = datetime.time(14, 30, 15)
print(specific_time)

specific_datetime = datetime.datetime(2025, 2, 17, 4, 30, 15)
print(specific_datetime)

now = datetime.datetime.now()
formatted = now.strftime("%Y-%m-%d %H:%M:%S")
print(formatted)

date_str = "2025-05-19 15:54:36"
parse_time = datetime.datetime.strptime(date_str, "%Y-%m-%d %H:%M:%S")
print(parse_time)

noww =datetime.datetime.now()
delta=datetime.timedelta(days=10)

future_date = noww + delta
past_date =noww - delta
print(f"future date {future_date}")
print(f"past date {past_date}")

#i want dates between toeay and last 5 days
from datetime import datetime,timedelta
datetime
today = datetime.now()
dates = [today - timedelta(days = i) for i in range(6)]
print(dates)


format_date = [datetime.strftime("%y-%m-%d") for datetime in dates]
print(format_date)

#Accessing individual dates
nowwwww = datetime.now()
print("year", nowwwww.year)
print("month", nowwwww.month)
print("day", nowwwww.day)
print("hour", nowwwww.hour)
print("minute", nowwwww.minute)
print("second", nowwwww.second)

