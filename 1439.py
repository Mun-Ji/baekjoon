import sys
a=sys.stdin.readline().strip()
count=0
for i in range(len(a)-1):
    if a[i] != a[i+1]:
        count+=1
if count%2==0:
    print(count//2)
else:
    print((count+1)//2)