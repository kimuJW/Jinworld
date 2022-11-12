T=int(input())
L=[]
for i in range(T):
    a,b=map(int,input().split())
    L.append(a)
    L.append(b)
for i in range(T):
    print(L[2*i]+L[2*i+1])