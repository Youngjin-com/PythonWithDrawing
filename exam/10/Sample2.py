import os
import os.path
import datetime

curdir = os.listdir(".")

print("이름", end="\t")
print("최종 액세스 시각")

for name in curdir:
    atime = os.path.getatime(name)

    print(name, end="\t")
    print(datetime.datetime.fromtimestamp(atime))
