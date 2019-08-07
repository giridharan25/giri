x,y=map(str,input().split())
count=0
c=len(x)
d=len(y)
for k in range(0,c):
    if(x[k]==y[k]):
        count+=1
o=(d-count)
print(o)    
