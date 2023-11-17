# 가장 큰 수 k번 더하고 그 다음 큰 수 1번 더하기
n, m, k = map(int, input().split())
data = list(map(int, input().split()))
# n만큼이 m만큼 더해지고 k만큼 연속가능한 큰수를 구할것
data.sort()
first = data[n-1]
second = data[n-2]

answer = 0

while True:
        
    for i in range(k): #m만큼 반복
       if m == 0:
           break
       answer += first
       m -= 1
       
    if m == 0: 
        break

    answer += second
    m -= 1

print(answer)