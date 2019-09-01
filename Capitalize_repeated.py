s=str(input())
h=len(s)
o=[]
for i in s:
    o.append(i)
for j in range(0,h):
    if(s.count(o[j])>1):
        	o[j]=o[j].upper()
for z in o:
   print(z,end="")
