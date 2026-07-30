class Solution(object):
    def nextGreaterElements(self, nums):
        stack=[]
        res=[]
        for j in range(len(nums)-2,-1,-1):
            stack.append(nums[j])
        for i in range(len(nums)-1,-1,-1):
            while stack and stack[-1]<=nums[i]:
                stack.pop()
            if stack and stack[-1]>nums[i]:
                res.append(stack[-1])
            if not stack:
                res.append(-1)
            stack.append(nums[i])
        return res[::-1]

