class Solution(object):
    def maxProduct(self, nums):
        minindex=nums[0]
        maxindex=nums[0]
        ans=nums[0]
        for i in range(1,len(nums)):
            op1=nums[i]
            op2=maxindex*nums[i]
            op3=minindex*nums[i]
            maxindex=max(op1,op2,op3)
            minindex=min(op1,op2,op3)
            ans=max(ans,maxindex)
        return ans

        
        
        