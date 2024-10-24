import os
import os.path

curdir = os.listdir(".")

print("이름", end="\t")
print("크기")

for name in curdir:
    print(name, end="\t")
    print(os.path.getsize(name), "바이트")
