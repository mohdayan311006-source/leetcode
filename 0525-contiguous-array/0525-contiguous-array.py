class Solution(object):
    def findMaxLength(self, nums):
        one=0
        zero=0
        res=0
        freq={}
        for i in range(len(nums)):
            if nums[i]==0:
                zero+=1
            else:
                one+=1
            diff=zero-one
            if diff==0:
                res=max(res,i+1)
            if diff in freq:
                lenght=i-freq[diff]
                res=max(res,lenght)
            else:
                freq[diff]=i
        return res
        
       

        