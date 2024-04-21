import sys
from itertools import combinations as coms
from itertools import permutations as perm
input=sys.stdin.readline
N=int(input())
scores=[list(map(int,input().split())) for _ in range(N)]
player=list(range(N))
poss_teams=list(coms(player,N//2))
poss_cnt=len(poss_teams)
mini=4500
for i in range(poss_cnt//2):
    a=poss_teams[i]
    b=poss_teams[-i-1]
    a_scores=perm(a,2)
    b_scores=perm(b,2)
    a_total=0
    b_total=0
    for i,j in a_scores:
        a_total+=scores[i][j]
    for i,j in b_scores:
        b_total+=scores[i][j]
    mini=min(mini,abs(a_total-b_total))
print(mini)