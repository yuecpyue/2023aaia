#SOIT106_BASE_011
a,b=list(map(int,input().split()))
if a<b:
	print(-1)
elif a==b:
	print(0)
else:
	print(1)