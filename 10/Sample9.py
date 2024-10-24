import datetime

dt = datetime.datetime.now()
str = dt.strftime("%c")
print("현재는", str, "입니다.")

dt = dt + datetime.timedelta(days = 1)
str = dt.strftime("%Y-%m-%d")
print("1일 후는", str, "입니다.")
