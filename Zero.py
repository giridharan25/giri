n=int(input())
l=list(map(int,input().split()))
s=[]
for i in l:
  for j in l[1:n]:
     if(i+j==0):
        
        s.append(i)
        s.append(j)
print(s[0],s[1])
