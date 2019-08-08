x,y=map(str,input().split())
y=int(y)
if(y==0):
    print(int(x))
else:
   h=len(x)
   g=h-y
   s=x[:g]
   small=int(s)
   l=[]
   l.append(small)
    
   for i in range(0,h-y):
       a=small
       f=int(x[i:i+y])
       if(a>f):
        l.append(f)
   l.sort()
   print(l)
   print(l[0])
