import sys
N=int(input())
count=0
for i in range(N):
    str=sys.stdin.readline()
    a=list(set(str))       
    for j in range(len(str)):  
        if str[j] in a:
            if j+1==len(str):
                break 
            elif str[j]!=str[j+1]:
                if str[j+1:].count(str[j])>=1:
                    count+=1
                    break              
print(N-count)