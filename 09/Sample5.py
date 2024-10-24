str1 = input("문자열을 입력하세요.")
old = input("치환되는 문자열을 입력하세요.")
new = input("치환하는 문자열을 입력하세요.")

if old in str1:
    str2 = str1.replace(old, new)
    print(str2, "로 치환했습니다.")
else:
    print(str1 + "의 안에서" + old + "를 발견했습니다.")
