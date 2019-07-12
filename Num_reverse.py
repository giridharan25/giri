g = int(input())

temp = g

rev = 0

while temp != 0:

	rev = (rev * 10) + (temp % 10)

	temp = temp // 10
	
print(rev)	
