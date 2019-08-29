x,y=map(int,input().split())
items=list(map(int,input().split()))
share=int(input())
a=items
a[y]=0
sum1=0
for i in a:
    sum1=sum1+i
    a_share=sum1/2
if(share==a_share):
    print("Bon Appetit")
else:
    print(round(share-a_share))
