import os
import os.path

curdir = os.listdir(".")

for name in curdir:
    print(os.path.abspath(name), end = ",")
    
    if(os.path.isfile(name)):
        print("파일입니다.")
    else:
        print("디렉터리입니다.")
print()
