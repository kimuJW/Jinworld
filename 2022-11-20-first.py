import sys
list=[]
for i in range(1,31):
    list.append(i)
for i in range(28):
    a=int(sys.stdin.readline())
    b=list.index(a)
    del list[b]
for i in range(len(list)):
    print(list[i])
