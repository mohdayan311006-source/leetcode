class Solution(object):
    def subarraySum(self, nums, k):
        mp={0:1}
        prefixsum=0
        count=0
        for i in range(len(nums)):
            prefixsum+=nums[i]
            if (prefixsum-k) in mp:
                count+=mp[prefixsum-k]
            mp[prefixsum] = mp.get(prefixsum, 0) + 1
        return count
