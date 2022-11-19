List=[]
for i in range(9):
    List.append(int(input()))
print(max(List))
print(int(List.index(max(List))+1))
