l,r=map(int,input().split())
output=0
n=100000
for i in range(1,n):
    if((i%l==0) and (i%r==0)):
        	output=i
        	break
print(output)
