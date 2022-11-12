T=int(input())
L=[]
L2=[]
for i in range(T):
    a,b=map(int,input().split())
    L.append(a+b)
    L2.append(a) 
    L2.append(b)
for i in range(T):
    print("Case #{}:".format(i+1), L2[2*i],"+",L2[2*i+1],"=",L[i])