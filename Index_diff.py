n=int(input())
o=list(map(int,input().split()))
small=o[0]
big=o[0]
for i in o:
  if(i<small):
      small=i
  if(i>big):
      big=i
a=o.index(small)
b=o.index(big)
c=a-b
print(abs(c))
