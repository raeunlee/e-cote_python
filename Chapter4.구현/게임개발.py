n, m = map(int, input().split())

d = [[0] * m for _ in range(n)]
x, y, dir = map(int, input().split())
d[x][y] = 1 #now

array = []
for i in range(n):
    array.append(list(map(int, input().split())))
    
dx = [-1,0,1,0] #북 동 남 서 
dy = [0,1,0,-1]

# 0 1 2 3 순 
def turn_left():
    global dir
    dir -= 1 #turn left
    if dir == -1: # -1면 3
        dir == 3

#start
count = 1
turn_time = 0

# start simul
while True:
    turn_left() # step 1!
    nx = x + dx[dir]
    ny = y + dy[dir]
    
    if d[nx][ny] == 0 and array[nx][ny] == 0: #step2 - yes
        d[nx][ny] == 1
        y = ny
        x = nx
        count += 1
        turn_time = 0
        continue
    
    else: #step2 - No
        turn_time +=1 
        
    if turn_time == 4: #step3
        nx = x - dx[dir] 
        ny = y - dy[dir]
        if array[nx][ny] == 0:  #뒤로 갈 수 있으면 
            y = ny
            x = nx
        else: 
            break #stop
        
        turn_time = 0
print(count)
        









