#191. Number of 1 Bits
class Solution:
    def hammingWeight(self, n: int) -> int:
        ans=0
        while n>0:#要把n剝光
            ans+=n%2#剝下來的皮
            n=n//2#剝完就除2

        return ans