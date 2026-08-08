class Solution(object):
    def maxNumberOfBalloons(self, text):
        req='balloon'
        have={}
        need={}
        ans=float('inf')
        for ch in text:
            have[ch]=have.get(ch,0)+1
        for ch in req:
            need[ch]=need.get(ch,0)+1
        for ch in need:
            ans=min(ans,have.get(ch,0)//need[ch])
        return ans
            
            
           
        



        