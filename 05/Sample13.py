city = ["서울", "대전", "대구", "부산"]
sale = [80, 60, 22, 50, 75]

print("도시명 데이터는", city, "입니다.")
print("매출 데이터는", sale, "입니다.")

print("데이터를 조합합니다.")

for d in zip(city, sale):
    print(d)

print("데이터를 분해합니다.")

for c, s in zip(city, sale):
    print("도시명은", c, "매출은", s)

