data = [1, 2, 3, 4, 5]
print("현재 데이터는", data, "입니다.")

ndata = [n * 2 for n in data if n != 3]

print("새로운 데이터는", ndata, "입니다.")
