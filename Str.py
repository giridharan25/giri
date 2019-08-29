x=str(input())
a=len(x)
e=[]
f=[" "]
o=[]
for i in range(0,a):
    if(i%2==0):
        e.append(x[i])
    else:
        o.append(x[i])
z=e+f+o
for j in z:
    print(j,end="")
