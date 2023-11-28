a=1500000000 #老大
b=2000000000 #老二
c=a%b #老三
print(a,b,c)
while c!=0:#輾轉相除法
  a=b
  b=c
  c=a%b
  print(a,b,c)
print(b)