import sys
input=sys.stdin.readline
n=int(input())
tree=[int(input()) for _ in range(n)]
tree_minus=[]
for i in range(len(tree)-1):
    tree_minus.append(tree[i+1]-tree[i])
tree_minus_a=tree_minus.copy()
while True:
    tree_minus_1=tree_minus.copy()
    mini=min(tree_minus_1)
    tree_minus.clear()
    for i in range(len(tree_minus_1)):
        if tree_minus_1[i]==mini:
            tree_minus.append(mini)
        else:
            if tree_minus_1[i]%mini==0:
                pass
            else:
                tree_minus.append(tree_minus_1[i]%mini)
    if len(set(tree_minus))==1:
        break
ans=[i//mini-1 for i in tree_minus_a]
print(sum(ans))