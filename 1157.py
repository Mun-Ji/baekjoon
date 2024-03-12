a=input()
b=a.upper()
dict={}
list=[]
for i in b:
    dict[i]=0
for i in b:
    dict[i]+=1
c=max(dict.values())
for key,value in dict.items():
    if value==c:
        list.append(key)
if len(list)==1:
    print(list[0])
else:
    print("?")