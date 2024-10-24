import re

ptr = "\.(csv|html|py)$"
str = ["Sample.csv", "Sample.exe", "test.py", "index.html"]

pattern = re.compile(ptr)
for valuestr in str:
    res = pattern.sub(".txt", valuestr)
    msg = "(변환 전)" + valuestr + "(변환 후)" + res
    print(msg)
