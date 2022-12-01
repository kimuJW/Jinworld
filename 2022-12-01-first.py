N=int(input())
for i in range(N):
    list=[]
    a,b=map(str,input().split())
    for i in range(len(b)):
        for c in range(int(a)):
            list.append(b[i])
    for d in range(len(list)):
        print(list[d],end='')
    print("")   