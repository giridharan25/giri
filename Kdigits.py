x,y=map(str,input().split())
y=int(y)
if(y==0):
    print(x)
else:
  l=[]
  for i in x:
    k=int(i)
    l.append(k)
  small=l[0]
  for j in l:
    if(j<small):
        small=j
  h=l.index(small)
  o=x[h:y+h]
  print(o)
