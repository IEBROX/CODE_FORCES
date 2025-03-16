a=list(map(int,input("").split()))
b=list(map(int,input("").split()))
c=list(map(int,input("").split()))
d=list(map(int,input("").split()))
e=list(map(int,input("").split()))
l=[a,b,c,d,e]
m=int()
n=int()
for i in range(5):
    for j in range(5):
        if l[i][j]==1:
            m=i
            n=j
print(abs(m-2)+abs(n-2))
