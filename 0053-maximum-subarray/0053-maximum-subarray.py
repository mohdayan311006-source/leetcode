class Solution(object):
    def maxSubArray(self, nums):
        bestindexSum=nums[0]
        ans=nums[0]
        for i in range(1,len(nums)):
            op1=bestindexSum+nums[i]
            op2=nums[i]
            bestindexSum=max(op1,op2)
            ans=max(ans,bestindexSum)
        return ans

