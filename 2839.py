n=int(input())
a=n//5
while True:
    b=n-5*a
    if b%3==0:
        answer=a+b//3
        break
    a-=1
    if a<0:
        answer=-1
        break
print(answer)

