count=0
N=int(input())
list=list(map(int,input().split()))
v=int(input())
for i in range(N):
    if list[i]==v:
        count+=1
print(count)