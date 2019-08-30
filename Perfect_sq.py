import math
x,y=map(int,input().split())
coun=0
for i in range(x,y+1):
    j = int(math.sqrt(i)) 
    if(i == j*j): 
       coun+=1
print(coun)
