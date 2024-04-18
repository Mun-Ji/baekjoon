import sys
input=sys.stdin.readline
m, n= map(int,input().split())
nums=[list(map(int,input().split())) for _ in range(m)]
real_max=max(map(max,nums))
def sum_1(i,j,k:list): #ㄱ
    return [((i,j), (i,j+1), (i+1,j)), k[i][j]+k[i][j+1]+k[i+1][j]]
def sum_2(i,j,k:list): #좌우 뒤집힌 ㄴ
    return [((i,j+1), (i+1,j), (i+1,j+1)), k[i][j+1]+k[i+1][j]+k[i+1][j+1]]
def sum_3(i,j,k:list): #ㄴ
    return [((i,j), (i+1,j), (i+1,j+1)), k[i][j]+k[i+1][j]+k[i+1][j+1]]
def sum_4(i,j,k:list): #좌우 뒤집힌 ㄱ
    return [((i,j), (i,j+1), (i+1,j)), k[i][j]+k[i][j+1]+k[i+1][j]]
def sum_5(i,j,k:list): #가로 -
    return [((i,j), (i,j+1), (i,j+2)), k[i][j]+k[i][j+1]+k[i][j+2]]
def sum_6(i,j,k:list): #세로 ㅣ
    return [((i,j), (i+1,j), (i+2,j)), k[i][j]+k[i+1][j]+k[i+2][j]]

def max_tet(a,k:list):  #a는 sum 함수 중 하나
    poss=set()
    num=set()
    for r,s in a[0]:
        new=[(r-1,s),(r+1,s),(r,s-1),(r,s+1)]
        poss.update(new)
    for t in range(3):
        poss.remove(a[0][t])
    poss_list=list(poss)
    for i,j in poss_list:
        if i==-1 or j==-1:
            continue
        try:
            num.add(k[i][j])
        except IndexError:
            pass
    return a[1]+max(num)
if n==1:
    max_list=[]
    for i in range(m-3):
        max_list.append(sum(nums[i]+nums[i+1]+nums[i+2]+nums[i+3]))
    max_new=max(max_list)
elif n>=3:
    max_list=[]
    max_list.append(max_tet(sum_1(0,0,nums),nums))
    max_list.append(max_tet(sum_2(0,0,nums),nums))
    max_list.append(max_tet(sum_3(0,0,nums),nums))
    max_list.append(max_tet(sum_4(0,0,nums),nums))
    max_list.append(max_tet(sum_5(0,0,nums),nums))
    max_list.append(max_tet(sum_6(0,0,nums),nums))
    max_new=max(max_list)
    for i in range(m-1):
        for j in range(n-1):
            max_list.clear()
            max_1=sum_1(i,j,nums)[1]
            if max_1 <= max_new - real_max:
                pass
            else: 
                max_list.append(max_tet(sum_1(i,j,nums),nums))
            max_2=sum_2(i,j,nums)[1]
            if max_2 <= max_new - real_max:
                pass
            else: 
                max_list.append(max_tet(sum_2(i,j,nums),nums))
            max_3=sum_3(i,j,nums)[1]
            if max_3 <= max_new - real_max:
                pass
            else: 
                max_list.append(max_tet(sum_3(i,j,nums),nums))
            max_4=sum_4(i,j,nums)[1]
            if max_4 <= max_new - real_max:
                pass
            else: 
                max_list.append(max_tet(sum_4(i,j,nums),nums))
     
            if max_list!=[]: 
                max_cand=max(max_list)
                if max_cand > max_new:
                    max_new= max_cand
                
    for i in range(m-2):
        for j in range(n):
            max_list.clear()
            max_6=sum_6(i,j,nums)[1]
            if max_6 <= max_new - real_max:
                pass
            else: 
                max_list.append(max_tet(sum_6(i,j,nums),nums))
            if max_list!=[]: 
                max_cand=max(max_list)
                if max_cand > max_new:
                    max_new= max_cand

    for i in range(m):
        for j in range(n-2):
            max_list.clear()
            max_5=sum_5(i,j,nums)[1]
            if max_5 <= max_new - real_max:
                pass
            else: 
                max_list.append(max_tet(sum_5(i,j,nums),nums))
            if max_list!=[]: 
                max_cand=max(max_list)
                if max_cand > max_new:
                    max_new= max_cand
else: #n:2 
    max_list=[]
    max_list.append(max_tet(sum_1(0,0,nums),nums))
    max_list.append(max_tet(sum_2(0,0,nums),nums))
    max_list.append(max_tet(sum_3(0,0,nums),nums))
    max_list.append(max_tet(sum_4(0,0,nums),nums))
    max_list.append(max_tet(sum_6(0,0,nums),nums))
    max_new=max(max_list)
    for i in range(m-1):
        max_list.clear()
        max_1=sum_1(i,0,nums)[1]
        if max_1 <= max_new - real_max:
            pass
        else: 
            max_list.append(max_tet(sum_1(i,0,nums),nums))
        max_2=sum_2(i,0,nums)[1]
        if max_2 <= max_new - real_max:
            pass
        else: 
            max_list.append(max_tet(sum_2(i,0,nums),nums))
        max_3=sum_3(i,0,nums)[1]
        if max_3 <= max_new - real_max:
            pass
        else: 
            max_list.append(max_tet(sum_3(i,0,nums),nums))
        max_4=sum_4(i,0,nums)[1]
        if max_4 <= max_new - real_max:
            pass
        else: 
            max_list.append(max_tet(sum_4(i,0,nums),nums))
        if max_list!=[]: 
            max_cand=max(max_list)
            if max_cand > max_new:
                max_new= max_cand
    for i in range(m-2):
        for j in range(2):
            max_list.clear()
            max_6=sum_6(i,j,nums)[1]
            if max_6 <= max_new - real_max:
                pass
            else: 
                max_list.append(max_tet(sum_6(i,j,nums),nums))
            if max_list!=[]: 
                max_cand=max(max_list)
                if max_cand > max_new:
                    max_new= max_cand

print(max_new)