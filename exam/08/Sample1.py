class Car():

    def __init__(self, num, gas):
        self.num = num
        self.gas = gas
    def getNumber(self):
        return self.num

    def getGas(self):
       return self.gas

cr1 = Car(1234, 25.5)
n1 = cr1.getNumber()
g1 = cr1.getGas()

cr2 = Car(2345, 30.5)
n2 = cr2.getNumber()
g2 = cr2.getGas()

print("번호는", n1, "가솔린 양은", g1, "입니다.")
print("번호는", n2, "가솔린 양은", g2, "입니다.")
