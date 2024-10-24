data = [1, 2, 3, 4, 5]
print("현재 데이터는", data, "입니다.")

print("data[::-1]을 for 문으로 처리합니다.")
for d in data[::-1]:
    print(d)
print("data[::-1]은", data[::-1], "입니다.")
print("현재 데이터는", data, "입니다.")

print("reversed(data)를 for 문으로 처리합니다.")
for d in reversed(data):
    print(d)
print("reversed(data)는", reversed(data), "입니다.")
print("현재 데이터는", data, "입니다.")

print("data.reverse()를 처리합니다.")
data.reverse()
print("현재 데이터는", data, "입니다.")
