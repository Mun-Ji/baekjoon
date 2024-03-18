import sys
input=sys.stdin.readline
N=int(input())
time=[list(map(int,input().split())) for _ in range(N)]
time.sort(key=lambda x: (x[1],x[0]))
path=[]
while len(time) > 1:
    start=time[0]
    path.append(start)
    del time[0]
    while time[0][0] < start[1]:
        del time[0]
        if len(time)==0:
            break
if len(time)==1:
    path.append(time[0])
print(len(path))