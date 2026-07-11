class Solution(object):
    def pivotIndex(self, nums):
        left=0
        array_sum=sum(nums)
        for i in range(len(nums)):
            right=array_sum-nums[i]-left
            if left==right:
                return i
            left+=nums[i]
        return -1

       
            



        