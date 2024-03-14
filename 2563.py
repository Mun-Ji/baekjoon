import sys
arr=[0]*10000
n=int(input())
paper=[list(map(int,sys.stdin.readline().split())) for _ in range(n)]
for i in range(n):
    a,b=paper[i]
    for j in range(10):
        arr[(b+j)*100+a:(b+j)*100+a+10]=[1]*10
print(arr.count(1))