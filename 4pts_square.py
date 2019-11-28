x1,y1=map(int,input().split())
a1,b1=map(int,input().split())
x2,y2=map(int,input().split())
a2,b2=map(int,input().split())
x=abs(x1-x2)
y=abs(y1-y2)
a=abs(a1-a2)
b=abs(b1-b2)
if(x==y) and (a==b):
   print('yes')
else:
   print('no')
