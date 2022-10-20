N=int(input())
list=[]
def Han(n):
    if n<100: 
        list.append(n)
    elif n>=100 and n<=1000:
        if abs(n%10+n//100)/2==(n%100)//10:
            list.append(n)

for i in range(1,N+1):
    if i==1000:
        break
    Han(i)
print(len(list))