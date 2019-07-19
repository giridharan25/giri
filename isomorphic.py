x,y=list(input().split())
if(len(x)==len(y)):
    for i in range(0,len(x)):
        if(y[i]==y[i+1] and x[i]==x[i+1]):
            print("yes")
            break
        else:
            print("no")
else:
    print("no")
