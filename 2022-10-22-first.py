List=[]
List2=[]

def d(n):
    N=n+(n//1000+((n%1000)//100)+((n%100)//10)+n%10)     
    List.append(N)

for i in range(1,10000):
    List2.append(i)
for i in range(1,10000):
    d(i)

SetList = set(List)
SetList2 = set(List2)
List3=list(SetList2-SetList)
List3.sort()

for i in range(len(List3)):
    print(List3[i])