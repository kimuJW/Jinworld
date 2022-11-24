N = int(input())
for i in range(N):
    List=[]
    count=0
    List=list(map(int,input().split()))
    avg=sum(List[1:])/List[0]
    for a in range(1,len(List)):
        if List[a]>avg:
            count+=1 
    a=(count/List[0])*100
    print(f'{a:.3f}%')