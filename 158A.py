a=list(map(int,input("").split()))
b=list(map(int,input("").split()))
i=0
z=b.count(0)
h=a[1]-1
k=a[1]
if b[h]!=0:
    k=a[1]
    while h+1+i<a[0] and b[h]==b[h+1+i] and b[h]!=0:
        i+=1
        k+=1
elif b[h]==0 and z<len(b):
    k=len(b)-z
else:    
    k=0
print(k)
    