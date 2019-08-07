n=int(input())
lst=list(map(int,input().split()))

l=[]
s=[]

a=len(lst)
b=a+1
for i in range(0,a-1):
    for j in range(1,a):
        for k in range(2,a):
            s=[]
            if(lst[i]<lst[j]<lst[k]):
                               
                s.append(lst[i])
                s.append(lst[j])
                s.append(lst[k])
                if(s  not in l):
                   l.append(s)



print(len(l))
