N=int(input())
for i in range(N):
    a="*"*(i+1)
    if i==N-1:
        print(a.rjust(N),end='')
    else:
        print(a.rjust(N))