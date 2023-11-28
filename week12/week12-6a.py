def gcd(a,b):
  print(a,b)
  if a==0: return b
  if b==0: return c
  return gcd(b,a%b)

a=1500000000 #老大
b=2000000000 #老二
print(gcd(a,b))