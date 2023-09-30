n = int(input()) 
dir = input().split()

dx = [0,0,-1,1]
dy = [-1,1,0,0]
types = ['L', 'R', 'U', 'D']
x,y = 1,1 #start point
for d in dir:
    for i in range(len(types)):
        if d == types[i]:
            nx = x + dx[i]
            ny = y + dy[i]
    if nx < 1 or ny < 1 or nx > n or ny > n:
        continue 
    x, y = nx, ny
    
print(x,y)
        
    