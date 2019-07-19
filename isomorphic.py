x,y = input().split()
if len(x) != len(y):
    print("No")
else:
    for i in range(0,len(x)):
        if x.count(x[i])==y.count(y[i]):
            print("yes")
            break
        else:
            print("no")
            break
