class Person:

    def getName(self):
        return self.name

    def getAge(self):
       return self.age

pr = Person()
pr.name = "김영진"
pr.age = 23

n = pr.getName()
a = pr.getAge()

print(n, "씨는", a, "세입니다.")
