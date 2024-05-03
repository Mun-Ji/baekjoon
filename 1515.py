from itertools import combinations as coms
a=input()
li_num=list(a) #str
k=len(li_num)
current=1
i=0
def count(num:int):
    current_str=list(coms(str(current),num))
    return tuple(li_num[i:i+num]) in current_str



while i<k:
    if current<10:
        if count(1):
            i+=1
        current+=1
    elif current<100:
        if i<=k-2:
            if count(2):
                i+=2
            elif count(1):
                i+=1
            current+=1
        else:
            if count(1):
                i+=1
            current+=1
    elif current<1000:
        if i<=k-3:
            if count(3):
                i+=3
            elif count(2):
                i+=2
            elif count(1):
                i+=1
            current+=1
        elif i==k-2:
            if count(2):
                i+=2
            elif count(1):
                i+=1
            current+=1
        else:
            if count(1):
                i+=1
            current+=1
    elif current<10000:
        if i<=k-4:
            if count(4):
                i+=4
            elif count(3):
                i+=3
            elif count(2):
                i+=2
            elif count(1):
                i+=1
            current+=1
        elif i==k-3:
            if count(3):
                i+=3
            elif count(2):
                i+=2
            elif count(1):
                i+=1
            current+=1
        elif i==k-2:
            if count(2):
                i+=2
            elif count(1):
                i+=1
            current+=1
        else:
            if count(1):
                i+=1
            current+=1
    else:
        if i<=k-5:
            if count(5):
                i+=5
            elif count(4):
                i+=4
            elif count(3):
                i+=3
            elif count(2):
                i+=2
            elif count(1):
                i+=1
            current+=1
        elif i==k-4:
            if count(4):
                i+=4
            elif count(3):
                i+=3
            elif count(2):
                i+=2
            elif count(1):
                i+=1
            current+=1
        elif i==k-3:
            if count(3):
                i+=3
            elif count(2):
                i+=2
            elif count(1):
                i+=1
            current+=1
        elif i==k-2:
            if count(2):
                i+=2
            elif count(1):
                i+=1
            current+=1
        else:
            if count(1):
                i+=1
            current+=1

print(current-1)
