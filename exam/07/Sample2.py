def rpstr(num, str="*"):
    print(str * num)

s = input("문자열을 입력하세요.")
n = int(input("개수를 입력하세요."))

print("문자열 있음---")
rpstr(n, s)

print("문자열 없음---")
rpstr(n)
