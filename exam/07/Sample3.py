def makex(x):
    while True:
        yield x
        x = x+1

start = int(input("시작값(정수)를 입력하세요."))
stop = int(input("정지값(정수)를 입력하세요."))

for n in makex(start):
    if n >= stop:
        break
    print(n)
