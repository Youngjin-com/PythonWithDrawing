try:
    f = open("Sample.txt", "r")
   
except FileNotFoundError:
    print("파일을 오픈할 수 없었습니다.")

else:
    lines = f.readlines()
    for line in lines:
       print(line, end = "")
    f.close()

finally:
    print("처리를 종료합니다.")
