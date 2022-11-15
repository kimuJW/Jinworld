count=0
N=int(input())
n=N
if N<0 or N>99: 
    exit()        
while True:     
    a=(N%10)*10+(N//10+N%10)%10
    count+=1
    if a!=N:
        N=a                  
    if a==n:
        break   
print(count)