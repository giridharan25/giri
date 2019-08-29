n=int(input())
l = list(map(int,input().split()))
pl = [l[i:i+2] for i in range(0,len(l),2)]
for i in pl:
    if(len(i)==2): 
      i[0],i[1] = i[1],i[0]
zpl = [i for sublist in pl for i in sublist]  
for j in zpl:
    print(j,end=" ")
