n=int(input(""))
x=0
ls=[n]
for i in range(n):
    i=input("")
    ls.append(i)
    if i.startswith("++") or i.endswith("++"):
        x+=1
    else:
        x-=1
print(x)