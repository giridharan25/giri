n=int(input())
l=list(map(int,input().split()))
odd=[]
even=[]
for i in range(0,len(l)):
   if(i%2==0):
      odd.append(l[i])
   else:
      even.append(l[i])
odd.sort()
even.sort()
o=[]
z=0
y=0
for j in range(0,len(l)):
   if(j%2==0):
       o.append(odd[z])
       z=z+1
   else:
       o.append(even[y])
       y=y+1
for x in range(0,len(o)):
    if(x==len(o)-1):
        print(o[x],end="")
    else:
        print(o[x],end=" ")
