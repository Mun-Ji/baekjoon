import sys
input=sys.stdin.readline
sys.setrecursionlimit(110000)
N,M,R=map(int,input().split())
list_1=[map(int,input().split()) for _ in range(M)]
dict={}
for i in range(1,N+1):
    dict[i]=[]
for i,j in list_1:
    dict[i].append(j)
    dict[j].append(i)
for i in range(1,N+1):
    dict[i].sort()
V=[0]*N
count=1
def dfs(R:int):
    global V
    global count
    if V[R-1]==0:
        V[R-1]=count
        count+=1
    if dict[R]==[]:
        return
    for i in dict[R]:
        if V[i-1]==0:
            dfs(i)
    return
dfs(R)
print(*V,sep='\n')