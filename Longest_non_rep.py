s=str(input())
h=len(s)
sub=0
for i in range(0,len(s)):
   o=[]
   for j in s[i:h]:
       if(j not in o):
          o.append(j)
       else:
          break
       if(sub<len(o)):
          sub=len(o)
print(sub)
