s=int(input())
n=input()
l=[]

for i in n:
    l.append(i)
for j in l:
    a=l.count(j)
    if (a>1):        
        b=j
        break
print(b)  
