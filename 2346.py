import sys
input=sys.stdin.readline
n=int(input())
bal=list(map(int,input().split()))
bal_list=[]
for i in range(n):
    bal_list.append([bal[i],i+1])
point=0
while True:
    move=bal_list[point][0]
    print(bal_list[point][1], end=' ')
    del bal_list[point]
    if len(bal_list)==0:
        break
    if move > 0:
        point=(point+move-1)%len(bal_list)
    else:
        point=(point+move)%len(bal_list)
