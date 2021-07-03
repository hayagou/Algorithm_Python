#[?] n명의 점수 중에서 80점 이상 95점 이하인 점수의 평균

# 평균 알고리즘(AverageAlgorithm) : 주어진 범위에 주어진 조건에 해당하는 자료들의 평균
# 평균 알고리즘의 특징 : SUM 과 COUNT 알고리즘의 조합 
#[1] Input : n명의 성적
data = [ 90, 65, 78, 50, 95 ]
sum = 0 # 합계 변수
count = 0 # 개수 변수
N = len(data) # 의사코드(슈도코드)
#[2] Process : AVG = SUM / COUNT

for i in range(0, N): # 주어진 범위
    if data[i] >= 80 and data[i] <= 95: # 주어진 조건
        sum += data[i] # SUM
        count += 1 # COUNT

avg = 0.0
if sum != 0 and count != 0 :
    avg = sum/ count # AVERAGE
#[3] Output
print(f"80점 이상 95점 이하인 자료의 평균 : {avg:.2f}")