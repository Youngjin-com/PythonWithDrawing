class Person:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def getName(self):
        return self.name

    def getAge(self):
        return self.age

pr = Person("김영진", 23)

n = pr.getName()
a = pr.getAge()

print(n, "씨는", a, "세입니다.")
