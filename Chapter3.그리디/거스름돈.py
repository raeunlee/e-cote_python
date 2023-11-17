# 500, 100, 50, 10
# 거슬러줘야 할 돈 N원, 동전 개수 최소로 쓰기

N = int(input())

coins = [500,100,50,10]

sum = 0

for coin in coins:
    sum += N // coin
    N = N % coin
    
print(sum) 