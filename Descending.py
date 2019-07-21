n=int(input())
a=list(map(int,input().split()))
a.sort()
a1=a[::-1]
if(a1[0]!=0):
    print(*a1,sep="")
else:
    print("0")
