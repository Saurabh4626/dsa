class Solution:
    def lengthOfLIS(self, nums) -> int:
        n=len(nums)
        dp=[1]*n
        for i in range(1,n):
            j=i
            while j>=0:
                if nums[j]<nums[i]:
                    dp[i]=max(dp[j]+1,dp[i])
                j-=1
        return max(dp)