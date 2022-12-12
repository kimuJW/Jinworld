N=int(input())
i=0
sum=1
while True:
    sum+=(6*i) #6 12 18 24 30 36 42 
    if sum>=N:
        i+=1
        break
    i+=1
print(i)