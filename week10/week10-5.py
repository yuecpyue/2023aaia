class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        a=arr
        N=len(a)

        a.sort()
        #for k in range(N-1):
            #for i in range(N-1):
                #if a[i+1]<a[i]:
                     #a[i],a[i+1]=a[i+1],a[i]
        for i in range(N-1):
            d=a[1]-a[0]#基礎的距離
            if a[i+1]-a[i]!=d:
                return False

        return True