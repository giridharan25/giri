#giri
n=int(input())
l=list(map(int,input().split()))
for i in range(0,n):
  for j in range(1,n):
    for k in range(2,n):
       if(l[i]<l[j]<l[k]):
           if(l[i]+l[j]==l[k]):
               print(l[i],l[j],l[k])
