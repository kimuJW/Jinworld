List=[]
for i in range(10):
    List.append(int(input())%42)
List=set(List)
List2=list((List))
print(len(List2))