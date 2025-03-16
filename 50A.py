a=list(map(int,input("").split()))
if 0<a[0]<17 and 0<a[1]<17:
    area=a[0]*a[1]
    n=area//2
    print(n)
else:
    print("wrong input")
