a = 0

def funcB():

    b = 1
   
    print("funcB의 안에서는 변수a와 변수b를 사용할 수 있습니다.")
    print("변수 a의 값은", a, "입니다.")
    print("변수 b의 값은", b, "입니다.")
    #print("변수 c의 값은", c, "입니다.")

def funcC():

    c = 2
   
    print("funcC의 안에서는 변수 a와 변수 c를 사용할 수 있습니다.")
    print("변수 a의 값은", a, "입니다.")
    #print("변수 b의 값은", b, "입니다.")
    print("변수 c의 값은", c, "입니다.")


print("함수 밖에서 변수 a를 사용할 수 있습니다.")
print("변수 a의 값은", a, "입니다.")
#print("변수 b의 값은", b, "입니다.")
#print("변수 c의 값은", c, "입니다.")

funcB()
funcC()
