a,d=map(int,input().split())
f=[]
for b in range (a,d+1):
    for c in range(2,b):
        if (b%c==0):
            break
        else:
            f.append(b)
print(len(f))
