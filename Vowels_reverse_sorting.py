n=int(input())
l=[]
for z in range(0,n):
    g=str(input())
    l.append(g)
v=["a","e","i","o","u","A","E","I","O","U"]
o={}
m=[]
a=[]
for i in l:
   s=i
   coun=0
   for j in v:
      coun=coun + s.count(j)
   o[coun]=i
   m.append(coun)
m.sort(reverse=True)
for k in m:
   q=o[k]
   a.append(q)
for f in a:
   print(f)
