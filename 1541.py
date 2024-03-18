import sys
input=sys.stdin.readline
list_num=input().split('-')
new_list=[]
for i in range(len(list_num)):
    new_list.append(list(map(int, list_num[i].split('+'))))
answer=0
answer+=sum(new_list[0])
for i in range(1,len(new_list)):
    answer-=sum(new_list[i])
print(answer)