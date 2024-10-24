num = int(input("몇 월의 처리를 건너뛸까요?(1～12)"))

for i in range(12):
    if (i + 1) == num:
        continue
    print(i + 1, "월의 데이터입니다.")
