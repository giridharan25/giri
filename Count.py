x,y=map(int,input().split())
mark=y
m=list(map(int,input().split()))
o=m.count(mark)
if(o==0):
    print(-1)
else:
    print(o)
