N=int(input())
S=str(input())
if (len(S)<=N):
    d=S.replace("a","")
    e=d.replace("A","")
    f=e.replace("e","")
    g=f.replace("E","")
    h=g.replace("i","")
    i=h.replace("I","")
    j=i.replace("o","")
    k=j.replace("O","")
    l=k.replace("u","")
    m=l.replace("U","")
    c=m[::-1]
    print(c)
