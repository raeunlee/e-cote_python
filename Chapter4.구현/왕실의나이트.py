data = input()
col = int(ord(data[0])) - int(ord('a')) + 1
row = int(data[1])
dir = [( -2, 1),(2, 1),(2, -1),(-2, -1),(1, 2),(-1,2),(1,-2),(-1,-2)]


r = 0

for d in dir: 
    nrow = row + d[0]
    ncol = col + d[1]
    if ncol >= 1 and nrow >=1 and ncol <= 8 and nrow <= 8:
        r += 1
    
print(r)