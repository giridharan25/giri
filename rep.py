s=int(input())
l=list(map(str,input().split()))
for j in l:
    a=l.count(j)
    if (a>1):        
        b=j
        break
print(b)  
