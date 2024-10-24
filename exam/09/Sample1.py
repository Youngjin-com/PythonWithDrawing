str = ["Sample.csv", "Sample.exe", 
       "Sample1.py", "Sample2.py",
       "Sample.txt","index.html"
      ]
file = []

print("파일의 리스트는 이하입니다.")

for s in str:
    print(s)

suf = input("확장자를 입력하세요.")

for s in str:
    res = s.endswith(suf)
    if res is True:
        file.append(s)

print("해당하는 파일의 리스트는 이하입니다.")

for f in file:
    print(f)
