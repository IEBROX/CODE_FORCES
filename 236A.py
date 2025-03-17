a=input("")
s=len(set(a))
if s%2!=0 and len(a)<101:
    print("IGNORE HIM!")
elif len(a)<101 and s%2==0:
    print("CHAT WITH HER!")
else:
    print("wrong")
