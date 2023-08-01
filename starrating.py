# import datetime
# today=datetime.date.today()
# birthday=datetime.date(2024,6,18)
# left=birthday-today
# print("left: ",left)
import calendar
import datetime
#
# y, m, d = map(int, input("Enter birthday [yyyy-mm-dd]: ").split('-'))
#
# w=datetime.date(y,m,d).weekday()
# print('Monday' if w==0 else 'Tuesday' if w==1 else 'Wednesday' if w==2 else 'Thurday' if w==3 else 'Friday' if w==4 else 'Saturday' if w==5 else 'Sunday')
# age=datetime.date.today()-datetime.date(y,m,d)
# print(age)
#
# year = datetime.date.today().year
# today = datetime.date.today()
# birthday = datetime.date(y, m, d)
#
# if today.month < m or (today.month == m and today.day < d):
#     next_birthday = datetime.date(year, m, d)
#     days_left = next_birthday - today
# else:
#     next_birthday = datetime.date(year + 1, m, d)
#     days_left = next_birthday - today
#
# if today == birthday:
#     print('Happy Birthday!')
# else:
#     print(next_birthday)
#     print("Days left: ", days_left)


# print(datetime.datetime.now())
# print(datetime.datetime.now().time())
# print(datetime.datetime.now()+datetime.timedelta(weeks=1))
# print(datetime.datetime.now()-datetime.timedelta(hours=48))

# import calendar
# y,m=map(int,input().split())
# print(calendar.month(y,m))
# print(calendar.isleap(y))
# w=calendar.weekday(y,m,1)
# print("Monday" if w==0 else 'Tuesday' if w==1 else 'Wednesday' if w==2 else 'Thursday' if w==3 else 'Friday' if w==4 else 'Saturday' if w==5 else 'Sunday')
# print(calendar.monthrange(y,m)[1])

# y,m,d=map(int,input().split())
# print(calendar.month(y,m))
# w=calendar.weekday(y,m,d)
# print("Monday" if w==0 else 'Tuesday' if w==1 else 'Wednesday' if w==2 else 'Thursday' if w==3 else 'Friday' if w==4 else 'Saturday' if w==5 else 'Sunday')
# print(calendar.isleap(y))
# print(datetime.date(y,m,d)-datetime.date.today())
# t=datetime.date.today()
# if t.month==m:
#     print(calendar.month(t.year,m))
# else:
#     print('It is not in current month!')


# import datetime
# timestamp = input("Enter an epoch timestamp: ")
# try:
#     dt = datetime.datetime.fromtimestamp(int(timestamp))
#     local_dt = dt.strftime("%Y-%m-%d %H:%M:%S")
#     print("Local Date and Time:", local_dt)
#     utc_dt = dt.strftime("%Y-%m-%d %H:%M:%S UTC")
#     print("UTC Date and Time:", utc_dt)
# except ValueError:
#     print("Invalid timestamp entered.")

import time
print('Stopwatch started.')
start=time.time()
input()
end=time.time()
print(round(end-start), "seconds")