s=str(input())
h=len(s)
o=[]

x=int(h/3)
if(h%3!=0):
  y=h%3
  f=s[0:y]
  o.append(f)
for i in range(0,x):
    a=s[h-3:h]
    o.append(a)
    h=h-3
for j in o:
    c=int(j,2)
    print(c,end="")
