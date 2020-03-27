a,b=input().split()
if(abs(len(a)-len(b))>=2):
    print("no")
elif(len(a)>len(b)):
   o=1
   for i in range(0,len(b)):
      if(a[i]!=b[i]):
          o=0
          break
   if(o==1):
       print("yes")
   else:
       print("no")
elif(len(a)>len(b)):
   o=1
   for j in range(0,len(a)):
      if(a[i]!=b[i]):
          o=0
          break
   if(o==1):
       print("yes")
   else:
       print("no")
elif(len(b)==len(a)):
   o=0
   for k in range(0,len(a)):
       if(a[k]!=b[k]):
           o=o+1
   if(o==1):
       print("yes")
   else:
       print("no")
