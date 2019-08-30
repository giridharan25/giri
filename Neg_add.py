n=int(input())
l=list(map(int,input().split()))
sum1=0
for i in l:
    if(i<0):
        sum1=sum1+i
print(sum1)
