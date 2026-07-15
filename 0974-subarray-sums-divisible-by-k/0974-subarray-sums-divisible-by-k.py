class Solution(object):
    def subarraysDivByK(self, nums, k):
        mp={0:1}
        count=0
        sum=0
        for i in range(len(nums)):
            sum+=nums[i]
            remainder=sum%k
            if remainder<0:
                remainder+=k
            if remainder in mp:
                count+=mp[remainder]
            mp[remainder]=mp.get(remainder,0)+1
        return count


        