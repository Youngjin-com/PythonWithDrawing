import re

ptr = ["(TXT)+", "TXT|XTX"]
str = ["TX", "TXT", "XTX", "TXTXT"]

for valueptr in ptr:
    print("------")
    pattern = re.compile(valueptr)
    for valuestr in str:
        res = pattern.search(valuestr)
        if res is not None:
            m = "〇"
        else:
            m = "×"
        msg = "(패턴)" + valueptr + "(문자열)" + valuestr + "(매치)" + m
        print(msg)
