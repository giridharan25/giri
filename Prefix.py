n=int(input())
a=[]
for i in range(0,n):
    string=str(input())
    a.append(string)
prefix_len = len(a[0]) 
for x in a[1 : ]:
    prefix_len = min(prefix_len, len(x)) 
    while not x.startswith(a[0][ : prefix_len]): 
         prefix_len -= 1 
prefix = a[0][ : prefix_len]
print(prefix)
