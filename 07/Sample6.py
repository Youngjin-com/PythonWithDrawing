def sell(place, price, num):
    print(place, "지점에서", num, "회사에", price, "만원 판매가 되었습니다.")
    tt = price * num
    return tt

total = sell("서울", 100, 5)

print("매출은 ", total, "만 원이었습니다.")
