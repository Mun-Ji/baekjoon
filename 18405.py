import sys
input=sys.stdin.readline
sys.setrecursionlimit(20000)
N,K=map(int,input().split())
point=[list(map(int,input().split())) for _ in range(N)]
S,X,Y=map(int,input().split())
no_zero=[]
for i in range(N):
    for j in range(N):
        if point[i][j]!=0:
            no_zero.append([i+1,j+1,point[i][j]])
ans=[abs(row-X)+abs(column-Y) for row,column,_ in no_zero]
time=min(ans)
if time > S:
    print(0)
else:
    same=[]
    for i in range(len(ans)):
        if ans[i]==time:
            same.append(no_zero[i][2])
    print(min(same))