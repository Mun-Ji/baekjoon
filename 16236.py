import sys
import copy
input=sys.stdin.readline
m=int(input())
map_li=[list(map(int,input().split())) for _ in range(m)]
for i in range(m**2):
    if map_li[i//m][i%m]==9:
        shark_wh=(i//m,i%m)
        break
size=2
time=0
eat=0
map_li[shark_wh[0]][shark_wh[1]]=0
dir=[(-1,0),(0,-1),(0,1),(1,0)]
num=0
while True:
    map_li_copy=copy.deepcopy(map_li)
    shark_loc=[shark_wh]
    map_li_copy[shark_wh[0]][shark_wh[1]]=-1
    dist=0
    shark_wh_cand=[]
    while True:
        k=len(shark_loc)
        for _ in range(k):
            a,b=shark_loc.pop()
            for i,j in dir:
                if 0<=a+i<=m-1 and 0<=b+j<=m-1:
                    if 1 <= map_li_copy[a+i][b+j] < size:
                        shark_wh_cand.append((a+i,b+j))
                    
                    elif 0<= map_li_copy[a+i][b+j] <= size:
                        map_li_copy[a+i][b+j]=-1
                        shark_loc.insert(0,(a+i,b+j))
                    else:
                        pass
        dist+=1

        if shark_wh_cand != []:
            shark_wh_cand.sort(key=lambda x: (x[0], x[1]))
            shark_wh=shark_wh_cand[0]
            eat+=1
            map_li[shark_wh[0]][shark_wh[1]]=0
            break

        elif shark_loc==[]:
            dist=-1
            break
    if eat==size:
        eat=0
        size+=1
    if dist==-1:
        break
    else: 
        time+=dist

print(time)