s=input()
l=[]
for i in s:
    if(i>='A' and i<='V'):
        d=chr(ord(i)+3)
        l.append(d)
    else:
        c=chr(ord(i)-23)
        l.append(c)   
for i in l:
    print(i,end="")
