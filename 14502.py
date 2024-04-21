import sys
from itertools import combinations as coms
import copy
input=sys.stdin.readline
M,N=map(int,input().split())
board=[list(map(int,input().split())) for _ in range(M)]
zeros=[]
twos=[] #virus
for i in range(M):
    for j in range(N):
        if board[i][j]==2:
            twos.append((i,j))
        elif board[i][j]==0:
            zeros.append((i,j))
poss_wall_list=list(coms(zeros,3))
dir=[(-1,0),(1,0),(0,-1),(0,1)]
def virus(a):
    new_board=copy.deepcopy(board)
    for i,j in a:
        new_board[i][j]=1
    total=1
    new_twos=twos
    while total!=0:
        total=0
        new=[]
        for i,j in new_twos:
            for d,s in dir:
                ni=i+d
                nj=j+s
                if 0<=ni<=M-1 and 0<=nj<=N-1 and new_board[ni][nj]==0:
                    total+=1
                    new_board[ni][nj]=2
                    new.append((ni,nj))
        new_twos=new
    return new_board

maxi=0
for i in poss_wall_list:
    a=virus(i)
    cnt=0
    for i in range(M):
        for j in range(N):
            if a[i][j]==0:
                cnt+=1
    maxi=max(maxi,cnt)
print(maxi)
