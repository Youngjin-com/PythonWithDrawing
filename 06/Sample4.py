sale = {"서울": 80, "대전": 60, "대구": 22, "부산": 50, "광주": 75}
print("현재 데이터는", sale, "입니다.")

print("키를 표시합니다.")
for k in sale.keys():
    print(k, end = "\t")
print()

print("값을 표시합니다.")
for v in sale.values():
    print(v, end = "\t")
print()

print("키와 값을 표시합니다.")
for i in sale.items():
    print(i, end = "")
print()
