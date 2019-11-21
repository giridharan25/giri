def gcd(a, b):
    while b > 0:
        a, b = b, a % b
    return a
a = list(map(int,input().split()))
result = a[0]
for i in a[1:]:
    result = gcd(result, i)
print(result)
