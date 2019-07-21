a=int(input())
b=list(map(int,input().split())
c=[]
for i in b:
    	if(b.count(i)>1 and i not in c):
        	c.append(i)
        	c.sort() 
if(len(c)==0):
    print("unique")
for j in c:
    print(j,end=" ")

