import sys
def blue(n,num):
    if all(num):
        return 1,0
    elif not any(num):
        return 0,1
    else:
        new1=[0]*((n//2)**2)
        new2=[0]*((n//2)**2)
        new3=[0]*((n//2)**2)
        new4=[0]*((n//2)**2)
        for i in range(n//2):
            new1[(n//2)*i:(n//2)*i+n//2]=num[n*i:n*i+n//2]
            new2[(n//2)*i:(n//2)*i+n//2]=num[n*i+n//2:n*i+n]
            new3[(n//2)*i:(n//2)*i+n//2]=num[n*((n//2)+i):n*((n//2)+i)+n//2]
            new4[(n//2)*i:(n//2)*i+n//2]=num[n*((n//2)+i)+n//2:n*((n//2)+i)+n]
        x=blue(n//2,new1)[0]+blue(n//2,new2)[0]+blue(n//2,new3)[0]+blue(n//2,new4)[0]
        y=blue(n//2,new1)[1]+blue(n//2,new2)[1]+blue(n//2,new3)[1]+blue(n//2,new4)[1]
        return x, y
a=int(input())
ls=[]
for i in range(a):
    ls+=list(map(int,sys.stdin.readline().split()))
print(blue(a,ls)[1])
print(blue(a,ls)[0])