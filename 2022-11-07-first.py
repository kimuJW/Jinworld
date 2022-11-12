x=int(input())
n=int(input())
L=[]
for i in range(n):
    a,b=map(int,input().split())
    L.append(a*b)
if sum(L)==x:
    print("Yes")
else:
    print("No")