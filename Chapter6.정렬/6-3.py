array = [7,9,8,4,5,6,3,1,2]

for i in range(1, len(array)): # i~
    for j in range(i,0,-1): # i -> 1
        if array[j] < array[j-1]:
            array[j], array[j-1] = array[j-1], array[j] 
        else:
            break
print(array)
        