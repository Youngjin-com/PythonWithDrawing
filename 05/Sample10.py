ysale = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
print("연간 데이터는", ysale, "입니다.")

sale1 = ysale[0:6]
print("상반기 데이터는", sale1, "입니다.")

sale2 = ysale[6:]
print("하반기 데이터는", sale2, "입니다.")

sale3 = ysale[::2]
print("1개월 거른 데이터는", sale3, "입니다.")

sale4 = ysale[::-1]
print("역순 데이터는", sale4, "입니다.")

print("연간 데이터는", ysale, "입니다.")
print("상반기 데이터를 바꿔 넣습니다.")
ysale[:6] = [0, 0, 0, 0, 0, 0]
print("연간 데이터는", ysale, "입니다.")
