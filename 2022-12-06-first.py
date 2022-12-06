str=input() 
list=['c=','c-','dz=','d-','lj','nj','s=','z=']
count=[]
length=[]
ans=[]
for i in range(len(list)):
    count.append(str.count(list[i]))
    length.append(count[i]*len(list[i])) 
    ans.append(-length[i]+count[i])   
print(len(str)+sum(ans)+(str.count('dz=')))