N=int(input())
List=list(map(int,input().split()))
M=max(List)
count=0
for i in range(len(List)):
    List[i]=List[i]/M*100
print(round(sum(List)/N,2))