import sys
input=sys.stdin.readline
m,n=map(int,input().split())
a,b,d=map(int,input().split())
map_list=[list(map(int,input().split())) for _ in range(m)]
dir=[(-1,0),(0,1),(1,0),(0,-1)]
n_loc=(a,b)
n_dir=d
ans=0
while True:
    if map_list[n_loc[0]][n_loc[1]]==0:
        map_list[n_loc[0]][n_loc[1]]=2
        ans+=1
    k=0
    for i in range(4):
        di=(n_dir-(i+1))%4
        loc=(n_loc[0]+dir[di][0],n_loc[1]+dir[di][1])
        try:
            if map_list[loc[0]][loc[1]]==0:
                n_dir=di
                n_loc=loc
                k=1
                break
        except IndexError:
            pass
        
    if k==0:
        loc=(n_loc[0]-dir[n_dir][0],n_loc[1]-dir[n_dir][1])
        try:
            if map_list[loc[0]][loc[1]]==1:
                break
            else:
                n_loc=loc
        except IndexError:
            break
print(ans)
