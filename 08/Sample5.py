class Person:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def getName(self):
        return self.name

    def getAge(self):
        return self.age

class Customer(Person):
    def __init__(self, nm, ag, ad, tl):
        super().__init__(nm, ag)

        self.adr = ad
        self.tel = tl

    def getName(self):
        return "고객: " + self.name

    def getAdr(self):
        return self.adr

    def getTel(self):
        return self.tel

pr = Customer("김영진", 23, "mmm@nnn.nn.kr", "xxx-xxx-xxxx")

nm = pr.getName()
ag = pr.getAge()
ad = pr.getAdr()
tl = pr.getTel()

print(nm, "씨는", ag, "세입니다.")
print("주소는", ad, "전화번호는", tl, "입니다.")
