a=input("").lower()
b=input("").lower()
if len(a)<101 and len(a)>0 and len(b)<101 and len(b)>0:
    if len(a)==len(b) and a==b:
        print("0") 
    elif a<b:
        print("-1")
    else:
        print("1")
else:
    print("wrong")