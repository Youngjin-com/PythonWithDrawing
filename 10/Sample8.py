import datetime

dt = datetime.datetime.now()
print("현재는", dt, "입니다.")
print("연: ", dt.year)
print("월: ", dt.month)
print("일: ", dt.day)

dt = dt + datetime.timedelta(days = 1)
print("1일 후는", dt, "입니다.")
