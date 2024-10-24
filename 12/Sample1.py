import statistics

data = [8, 17, 0, 11, 6, 21, 16, 6, 17, 11, 
        7, 9, 6, 13, 12, 16, 3, 14, 13, 12]

print("평균값은", statistics.mean(data), "입니다.")
print("중앙값은", statistics.median(data), "입니다.")
print("최빈값은", statistics.mode(data), "입니다.")
print("분산은", statistics.pvariance(data), "입니다.")
print("표준편차는", statistics.pstdev(data), "입니다.")
