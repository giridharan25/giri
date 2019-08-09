x,y=map(str,input().split())
sum1=0
sum2=0
for i in x:
  if(i not in y):
     sum1=sum1+ord(i)
for j in y:
  if(j not in x):
     sum2=sum2+ord(j)
o=sum2-sum1
p=o

print(p)
