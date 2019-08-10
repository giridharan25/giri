n=int(input())
l=list(map(int,input().split()))
s=[]
for i in range(0,n):
   if(i%2==0):
      if(l[i]%2!=0):
          s.append(l[i])
   else:
      if(l[i]%2==0):
          s.append(l[i])
for j in s:
   print(j,end=" ")
