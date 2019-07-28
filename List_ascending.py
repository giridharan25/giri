n=input()
l=list(map(str,input().split()))
l.sort(key=len)
print(*l, end=" "))
