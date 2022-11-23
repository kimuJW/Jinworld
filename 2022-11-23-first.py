N=int(input())
List=[]
sum=0
count=0
for i in range(N):
    List.append(input())
for i in range(len(List)):
    sum=0
    count=0
    for a in range(len(List[i])):    
        if List[i].find('O',a)==a:
            count+=1
            sum+=count
        elif List[i].index('X',a)==a:
            count=0
    print(sum)