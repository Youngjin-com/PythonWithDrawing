def deco(func):
    def wrapper(x):
        wx = "---" + x + "---"
        return func(wx)
    return wrapper

@deco
def printmsg(x):
    print(x, "를 입력했습니다.")

str = input("메시지를 입력하세요.")

printmsg(str)
