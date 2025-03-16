n=int(input(""))
ls=[]
a=[]
for i in range(n):
    s=input("")
    ls.append(s)
for w in ls:
    if len(w)>10:
        a=len(w)-2
        print(w[0]+str(a)+w[-1])
    else:
        print(w)