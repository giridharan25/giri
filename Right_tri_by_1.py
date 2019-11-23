n=int(input())
a="1"
l=["1"]
if(n>=1):
    for i in range(0,n-1):
          a=a+" 1"
          l.append(a)
    l=l[::-1]
    for j in l:
       print(j)
