class Solution(object):
    def numSubarrayProductLessThanK(self, nums, k):
        if k<=1:
            return 0
        count=0
        low=0
        product=1
        for high in range(len(nums)):
            product=product*nums[high]
            while product>=k:
                product=product/nums[low]
                low+=1
            count+=high-low+1
        return count

        


        