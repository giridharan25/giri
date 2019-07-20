n=int(input())
l=[]
for i in range(0,n):
    s=str(input())
    l.append(s)
f="kabali"
count=0
for j in l:
    if(sorted(f)==sorted(j)):
        count+=1
print(count)
