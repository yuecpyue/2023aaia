#SOIT108_Advance_010
a=input()
N=len(a)
for i in range(N):
	if (N-i)%3==0 and i!=0:
		print(',',end='')
	print(a[i],end='')