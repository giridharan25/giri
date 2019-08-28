n=int(input())
list1=list(map(int,input().split()))

o=[]
for i in list1:
    
    if(list1.count(i)==3):
        if(i not in o):
           o.append(i)
print(len(o))
