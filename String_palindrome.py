s=str(input())
n=int(input())
o=[]
for i in range(0,n):
   x=[]
   l,r=map(int,input().split())
   l=l-1
   r=r-1
   x.append(l)
   x.append(r)
   o.append(x)
for j in range(0,n):
  a=o[j][0]
  b=o[j][1]
  
  def reverse(t): 
      return t[::-1]
  
  def isPalindrome(t):
      rev = reverse(t)
      if (t == rev): 
            return True 
      return False
  t=s[a:b+1] 
  ans = isPalindrome(t) 

  if (ans == 1): 
       print("YES") 
  else: 
       print("NO")
