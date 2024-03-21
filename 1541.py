import sys
input=sys.stdin.readline
C, N=map(int,input().split())
city_list=[list(map(int,input().split())) for _ in range(N)]
dp=[]
for _ in range(N):
    dp.append([0]*C)
for i in range(N):
    for j in range(C):
        max=0
        if j+1 < city_list[i][1]:
            new=city_list[i][0]
        else:
            new = city_list[i][0] + dp[i][j-city_list[i][1]]
        if i == 0:
            dp[i][j]=new
        else:
            if new < dp[i-1][j]:
                dp[i][j]=new
            else:
                dp[i][j]=dp[i-1][j]
print(dp[N-1][C-1])

