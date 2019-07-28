n,m=map(int,input().split())
d=list(map(int,input().split()))
s=list(map(int,input().split()))
for i in s:
    if i in d:
        count="YES"
    else:
        count="NO"
        break
print(count) 
