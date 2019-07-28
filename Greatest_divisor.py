a,s=1,1
count=0
for i in range(1,s+1):
    if((a%i==0) and (s%i==0)):
       if(count<i):
           count=i
print(count)
