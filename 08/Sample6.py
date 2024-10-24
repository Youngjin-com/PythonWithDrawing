import myclass

pr = myclass.Customer("김영진", 23, "mmm@nnn.nn.kr", "xxx-xxx-xxxx")

nm = pr.getName()
ag = pr.getAge()
ad = pr.getAdr()
tl = pr.getTel()

print(nm, "씨는", ag, "세입니다.")
print("주소는", ad, "전화번호는", tl, "입니다.")
