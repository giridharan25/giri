n=int(input())
l=list(map(int,input().split()))
m=list(map(int,input().split()))
for i in range(0,n):
    if(l[i]!=i+1):
        red=l[i]-(i+1)
        m[i]=m[i]-abs(red)
for j in m:
   print(j,end=" ")
