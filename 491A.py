a=list(map(int,input("").split()))
i=0
if a[0]>0 and a[1]>0 and a[0]<11 and a[1]<11:
    while a[0]<a[1]+1:
        a[0]=a[0]*3
        a[1]=a[1]*2
        i+=1
print(i)