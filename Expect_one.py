a=int(input())
b=list(map(int,input().split()))
c=1
for i in b:
    if b.count(i)==c:
        j=i
print(j)
