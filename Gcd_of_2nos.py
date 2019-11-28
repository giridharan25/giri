x,y=map(int,input().split())
def gcd(a,b):
    if(b==0):
        return a
    else:
        return gcd(b,a%b)
GCD=gcd(x,y)
print(GCD)
