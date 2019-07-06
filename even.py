z=int(input("enter the number"))
result=z%2
if(z<=0):
    print("invalid")
else:
    if(result==0):
        print("Even")
    elif(result==1):
        print("Odd")
    else:
        print("invalid")
