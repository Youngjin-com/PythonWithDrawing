cityA = {"서울", "대전", "대구", "부산"}
cityB = {"대구", "부산", "광주"}

print("A의 도시명은", cityA, "입니다.")
print("B의 도시명은", cityB, "입니다.")

print("공통하는 데이터는", cityA & cityB, "입니다.")
print("A만의 데이터는", cityA - cityB, "입니다.")
print("B만의 데이터는", cityB - cityA, "입니다.")
print("모든 데이터는", cityA | cityB, "입니다.")
