s=input("")
n=len(s)
a=s.split("+")
m=int(max(a))
a.sort()
if n<101 and m<4:
    print("+".join(a))