a = 0

def func():
    global a
    b = 0
    
    print("변수 a는", a, "변수 b는", b)
    
    a = a + 1
    b = b + 1

for i in range(5):
    func()
