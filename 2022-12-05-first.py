A=input().upper()
Sum=0
for i in range(len(A)):
    if A[i]=='A'or A[i]=='B' or A[i]=='C':
        Sum+=2
    elif A[i]=='D'or A[i]=='E' or A[i]=='F':
        Sum+=3
    elif A[i]=='G'or A[i]=='H' or A[i]=='I':
        Sum+=4
    elif A[i]=='J'or A[i]=='K' or A[i]=='L':
        Sum+=5
    elif A[i]=='M'or A[i]=='N' or A[i]=='O':
        Sum+=6
    elif A[i]=='P'or A[i]=='Q' or A[i]=='R' or A[i]=='S':
        Sum+=7
    elif A[i]=='T'or A[i]=='U' or A[i]=='V':
        Sum+=8
    elif A[i]=='W'or A[i]=='X' or A[i]=='Y' or A[i]=='Z':
        Sum+=9
Sum+=len(A)
print(Sum)