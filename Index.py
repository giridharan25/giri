a=int(input())
b=list(map(int,input().split(None,a)[:a]))
a=[]
for i in range(len(b)):
    if b[i]==i:       
        a.append(b[i])
if len(a)==0:
    print(-1)
else:
    print(" ".join(map(str,a)))
