n=int(input())
l=list(map(int,input().split()))
sum1=0
s=[0]
f=s+l


for j in l:
   for k in f[0:j]:
       sum1=sum1+k
print(sum1)
