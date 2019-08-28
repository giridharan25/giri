n=int(input())
l=list(map(int,input().split()))
k=len(l)
l.sort()
for i in range(0,(k-2)):
    if(l[i]+l[i+1]==l[i+2]):
        o=l[i+2]
        break
print(o)
