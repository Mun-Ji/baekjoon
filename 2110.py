a=[(1,2),(3,4),(3,2),(2,1)]
a.sort(key=lambda x: (x[0],x[1]))
print(a)