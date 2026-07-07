class Solution(object):
    def maxAbsoluteSum(self, nums):
        minSum=nums[0]
        maxSum=nums[0]
        ans=abs(nums[0])
        for i in range(1,len(nums)):
            minSum=min(minSum+nums[i],nums[i])
            maxSum=max(maxSum+nums[i],nums[i])
            ans=max(ans,abs(minSum),abs(maxSum))
        return ans
            
            
        