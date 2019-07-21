n=int(input())
a=list(map(int,input().split()))
a.sort()
z=a[::-1]
if(z[0]!=0):
    print(*z,sep="")
else:
    print("0")
