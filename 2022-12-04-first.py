A,B=input().split()
if A[2]>B[2]:
    print(A[2],A[1],A[0],sep='')
elif A[2]==B[2] and A[1]>B[1]:
    print(A[2],A[1],A[0],sep='')
elif A[2]==B[2] and A[1]==B[1] and A[0]>B[0]:
    print(A[2],A[1],A[0],sep='')
else:
    print(B[2],B[1],B[0],sep='')