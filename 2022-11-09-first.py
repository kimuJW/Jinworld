T=int(input())
L=[]
for i in range(T):
    a,b=map(int,input().split())
    L.append(a+b)
for i in range(T):
    print("Case #{}:".format(i+1),L[i])