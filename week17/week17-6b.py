#SOIT108_Advance_012
K=int(input())
total=0
for i in range(1,1001):
	total+=i
	if total>K:
		ans=i
		break
print(ans,end='')