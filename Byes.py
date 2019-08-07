n=int(input())
a=[]
for i in range(0,n+1):
    b=2**i
    if(b<=n):
        a.append(b)
d=len(a)
c=n-a[d-1]    
print(c)
