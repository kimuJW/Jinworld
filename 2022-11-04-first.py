N,X=map(int,input().split())
list=list(map(int, input().split()))
store=[]
for i in range(N):
    if list[i]<X:
        store.append(list[i])
for i in range(len(store)):
    print(store[i],end=' ')