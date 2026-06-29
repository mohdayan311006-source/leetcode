class Solution(object):
    def maximumLengthSubstring(self, s):
        freq={}
        res=0
        low=0
        for high in range(len(s)):
            freq[s[high]]=freq.get(s[high],0)+1
            while freq[s[high]]>2:
                freq[s[low]]-=1
                if freq[s[low]]==0:
                    del freq[s[low]]
                low+=1

            res=max(res,high-low+1)
        return res
                

        
        