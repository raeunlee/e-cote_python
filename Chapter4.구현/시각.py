n = int(input())
count = 0 
for i in range(n+1): #hour
    for j in range(60): #minute
        for z in range(60): # second
            if '3' in str(i) + str(j) + str(z):
                count += 1
                
print(count)
        