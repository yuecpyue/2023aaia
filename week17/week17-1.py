class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        nums.sort()#數字排好
        ans=[[nums[0]]]
        repeat=0#目前數字num[0]沒有重復
        N=len(nums)
        for i in range(1,N):#想比較nums[i]vs. nums[i-1]是否相同
            if nums[i]==nums[i-1]:#這裡要處理，重複，相同，就repeat+=1
                repeat+=1
                if len(ans)<=repeat:
                    ans.append([])
            else:
                repeat=0
            ans[repeat].append(nums[i])

        return ans