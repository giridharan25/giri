a,s=map(int,input().split())
f=0
for i in range(a,s):
   for j in range(2,i):
     if (i%j==0):
        break
     else:
        f=f+1
 print(f)    

     
