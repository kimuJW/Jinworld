N=int(input())
n=0
sum=0
count=0
while True:  #2
    if count%2==1 and sum>=N:
        print(1+(sum%N),"/",n-(sum%N),sep='')
        break
    elif sum>=N:
        print(n-(sum%N),"/",1+(sum%N),sep='')
        break
    n+=1 
    sum+=n
    count+=1