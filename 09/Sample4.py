str = input("문자열을 입력하세요.")
key = input("검색하는 문자열을 입력하세요.")

res = str.find(key)

if res != -1:
    print(str, "의", res, "위치에서", key, "를 찾았습니다.")
else:
    print(str,  "의 안에서", key, "를 찾을 수 없었습니다.")
