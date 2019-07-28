import string
l=str(input())
l.translate({ord(c): None for c in string.whitespace})
print(l)
