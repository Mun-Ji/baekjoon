N=int(input())
if N==1:
    print(1)
elif N!=1:
    n=1
    while not N <= 1+3*(n**2)+3*n:
        n+=1
    print(n+1)