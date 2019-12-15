print("operation to be performed")
print("\n1.Store 2.Retrieve")
x=int(input())
name=[]
contact=[]
if(x==1):
   
   n=int(input("number of contacts to be stored now : ")
   for i in range(0,n):
       a=input("enter the name:")
       name.append(a)
       b=input("enter the contact:")
       contact.append(b)
if(x==2):
   n=int(input("number of contacts to be retrieve now : ")
   for j in range(0,n):
      names=input("enter the name:")
      ind=name.index(names)
      print(contact[ind])
