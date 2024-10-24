sale = [80, 60, 22, 50, 75]

i = int(input("몇 번의 데이터를 변경합니까?"))
num = int(input("변경 후의 데이터를 입력하세요."))

print(i, "번 데이터" , sale[i], "를 변경합니다.")

sale[i] = num

print(i, "번 데이터는", sale[i],  "(으)로 변경되었습니다.")
