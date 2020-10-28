s=input()
cur=0
pre=0
total=0
result=0
l=['I','V','X','L','C','D','M']
dic={'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
for i in range(len(s)):
    if(s[i] not in l):
        result=1
        break
    else:
        cur=dic[s[i]]
        if(cur>pre):
           total=total+cur-2*pre
        else:
           total=total+cur
if(result==0):           
    print(total)
else:
    print(-1)
