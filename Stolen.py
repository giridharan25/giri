no_of_batches=int(input())
o=[]
for i in range(0,no_of_batches):
    len_of_batch_1=int(input())
    batch_1=list(map(int,input().split()))
    new_batch_1=list(map(int,input().split()))
    for j in batch_1:
        if (j not in new_batch_1):
            z=batch_1.index(j)
            o.append(z)
for k in o:
    print(k)
