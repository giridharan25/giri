n=int(input())
l=list(map(str,input().split()))
res = sorted(l, key = lambda i: (len(i), i)) 
for j in res:
   print(j,end=" ")
