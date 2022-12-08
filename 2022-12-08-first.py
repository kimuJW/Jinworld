N,M=map(int,input().split())
c=[]
d=[]
for i in range(N):
    i=list(map(int,input().split()))
    c.append(i)
for i in range(N):
    i=list(map(int,input().split()))
    d.append(i)
for i in range(N):       
    for j in range(M):
        print(c[i][j]+d[i][j],end=" ")
    print()
