import sys
input=sys.stdin.readline
N,M=map(int,input().split())
house=[]
chicken=[]
for i in range(N):
    row=list(map(int,input().split()))
    for j in range(N):
        if row[j]==1:
            house.append([i,j])
        if row[j]==2:
            chicken.append([i,j])
def distance(house,chicken):
    dist=0
    for i,j in house:
        new=[]
        for k,l in chicken:
            new+=[abs(i-k)+abs(j-l)]
        dist+=min(new)
    return dist

from itertools import combinations as com
com_chicken=list(com(chicken,M))
ans=[]
for chicken_list in com_chicken:
    ans.append(distance(house,chicken_list))

print(min(ans))