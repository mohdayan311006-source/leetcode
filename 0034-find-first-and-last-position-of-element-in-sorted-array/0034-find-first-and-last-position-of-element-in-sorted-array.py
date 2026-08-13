class Solution(object):
    def searchRange(self, nums, target):
        def starting():
            ans=-1
            low=0
            high=len(nums)-1
            while low<=high:
                guess=(low+high)//2
                if nums[guess]==target:
                    ans=guess
                    high=guess-1
                elif nums[guess]>target:
                    high=guess-1
                else:
                    low=guess+1
            return ans
        def ending():
            low=0
            high=len(nums)-1
            ans=-1
            while low<=high:
                guess=(low+high)//2
                if nums[guess]==target:
                    ans=guess
                    low=guess+1
                elif nums[guess]>target:
                    high=guess-1
                else:
                    low=guess+1
            return ans
        return [starting(),ending()]




       
       

            
        
        