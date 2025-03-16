n=int(input(""))
ls=[]
a=0
for i in range(n):
    k=list(map(int,input("").split()))
    ls.append(k)
for q in ls:
    s=q.count(1)
    if s>1:
        a+=1      
print(a)