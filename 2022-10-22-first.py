array=[1,1,2,2,2,8]
array2=list(map(int,array))
input=list(map(int,input().split()))
print(int((array2[0]-input[0])), int((array2[1]-input[1])), int((array2[2]-input[2])), int((array2[3]-input[3])), int((array2[4]-input[4])), int(array2[5]-input[5]))