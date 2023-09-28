array = [7,9,8,4,5,6,3,1,2]

for i in range(len(array)): # i~
    min_index = i # temporary min_index 
    for j in range(i+1, len(array)): #i+1 ~ 
        if array[min_index] > array[j]: 
            min_index = j
    array[i], array[min_index] = array[min_index], array[i] #swap 
    
print(array)
            