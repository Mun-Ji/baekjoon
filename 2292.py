N=int(input())
a=1
b=7
count=0
while not a < N <= b:
    count+=1
    a+=count*6
    b+=(count+1)*6
ans = count + 2
print(ans)