num = int(input("몇 월의 처리에서 종료할까요?(1～12)"))

for i in range(12):
    print(i + 1, "월의 데이터입니다.")
    if (i + 1) == num:
        break
