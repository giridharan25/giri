str1=str(input())
list1=list(str1.split())
o=[]
for i in list1:
    a=i
    d="".join(sorted(a))
    o.append(d)
for j in o:
    print(j,end=" ")
