import sys
list1=[]
for i in range(9):
    list1.append(list(map(int,sys.stdin.readline().split())))
a=list1[0][0]
for i in range(len(list1)):
    for j in range(9):
        if list1[i][j]>=a:
            a=list1[i][j]
            x=i+1
            y=j+1
print(a)
print(x,y)