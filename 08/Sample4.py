class Person:
    count = 0

    def __init__(self, name, age):
        Person.count = Person.count + 1

        self.name = name
        self.age = age
      
    def getName(self):
        return self.name

    def getAge(self):
        return self.age

    @classmethod
    def getCount(cls):
        return cls.count

pr1 = Person("김영진", 23)
pr2 = Person("이지용", 38)

print(pr1.getName(), "씨는", pr1.getAge(), "세입니다.")
print(pr2.getName(), "씨는", pr2.getAge(), "세입니다.")
print("총 인원수는", Person.getCount(), "입니다.")
