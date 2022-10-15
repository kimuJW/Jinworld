a,b=map(int,input().split())
c=int(input())
if b+c/60==0:
 print(a,b+c)
elif b+c/60!=0:
    if a+((b+c)/60)>=24:
        print(abs(24-(a+(int((b+c)/60)))),(b+c)%60)
    else:
        print(a+(int((b+c)/60)),(b+c)%60)
