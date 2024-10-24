test = [74, 85, 69, 77, 81]

high = [t for t in test if t>=80]

print("테스트의 점수는", test, "입니다.")
print("80점 이상은", high, "입니다.")
print("80점 이상인 인원 수는", len(high), "입니다.")
