list=[]
while True: 
    A,B=map(int,input().split())
    if A+B!=0:
        list.append(A+B)
    else:
        break
for i in range(len(list)):
    print(list[i])