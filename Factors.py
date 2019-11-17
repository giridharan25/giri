n=int(input())
o=[]
for i in range(1,n+1):
   if(n%i==0):
     o.append(i)
for j in o:
   print(j,end=" ")
