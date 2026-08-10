class Solution(object):
    def longestPalindrome(self, s):
        have={}
        ans=0
        odd=False
        for i in range(len(s)):
            have[s[i]]=have.get(s[i],0)+1
        for ch in have:
            if have[ch]%2==0:
                ans+=have[ch]
            else:
                odd=True
        if odd==False:
            return ans
        for ch in have:
            if have[ch]%2==1:
                ans+=have[ch]-1
        return ans+1

        