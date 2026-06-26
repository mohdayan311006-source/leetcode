class Solution(object):
    def maximumSubarraySum(self, nums, k):
        freq={}
        low=0
        high=k-1
        sum=0
        res=0
        for i in range(0,high+1):
            freq[nums[i]]=freq.get(nums[i],0)+1
            sum+=nums[i]
        if len(freq)==k:
            res=max(res,sum)
        for high in range(k,len(nums)):
            freq[nums[high]]=freq.get(nums[high],0)+1
            sum+=nums[high]-nums[low]
            freq[nums[low]]-=1
            if freq[nums[low]]==0:
                del freq[nums[low]]
            if len(freq)==k:
                res=max(res,sum)
            low+=1
        return res


                


            
         
            

            
            
