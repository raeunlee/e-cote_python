# 연속되게 다른 부분은 하나로 본다

S = input()
count = 0
for i in range(len(S)-1):
    
    if S[i] != S[i+1]:
        count += 1
    
print((count+1)//2)