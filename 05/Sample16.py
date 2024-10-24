data = [
   ["서울", 32, 25], 
   ["대전", 28, 21], 
   ["대구", 27, 20],
   ["부산", 26, 19],
   ["광주", 27, 22]
]

print("현재 데이터는", data, "입니다.")

for dat in data:
   print("도시별 데이터는", dat, "입니다.")
   for d in dat:
      print(d, end = "\t")
   print()
   
print(data[0][0], "의 최고 기온은", data[0][1], "최저 기온은", data[0][2], "입니다.")
