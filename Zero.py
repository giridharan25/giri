n=int(input())
l=list(map(int,input().split()))
s=[]
f=[]
g=[]
for i in l:
  for j in l[1:n]:
     if((i+j==0)):
        s.append(i)
        s.append(j)
     elif(i+j==1):
        f.append(i)
        f.append(j)
     elif(i+j==-1):
        g.append(i)
        g.append(j)
a=len(s)
b=len(f)
if(a!=0):
    print(s[0],s[1])
elif(a==0):
    print(f[0],f[1])
else:
     print(g[0],g[1])
