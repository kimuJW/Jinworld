T=int(input())
count=0
for i in range(T):
    H,W,N = map(int,input().split())
    while True:
        count+=H       
        if count>=N:
            if N%H!=0:    
                print(101+((N%H-1)*100)+int(N/H))
                count=0
                break
            elif N%H==0:
                print(101+((H-1)*100)+int(N/H)-1)
                break