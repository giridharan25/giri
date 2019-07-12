a=input()
d=len(a)
x=0
for i in range(d):
   if(a=='IV'):
       x=4
   elif(a=='IX'):
       x=9
   elif(a=='XIV'): 
       x=14
   elif(a=='XIX'):
       x=19
   
   else:
     
     if(a[i]=="I"):
       x=x+1
     elif(a[i]=="V"):
       x=x+5
     elif(a[i]=="X"):
       x=x+10
print(x)  
