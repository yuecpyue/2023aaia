#因數 整除
a=120
#1 2 3 4 5 6 8 10.....for迴圈
ans = 0
for i in range(1,a+1):
  if a%i==0:
    print(i,end=' ')
    ans += 1 #迴圈 增加一
print(f'有幾個整除',ans)