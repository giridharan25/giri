a=list(input())
d=len(a)
new=''
for i in range (0,d,2):
    a[i],a[i+1]=a[i+1],a[i]

print(*a,sep='')
