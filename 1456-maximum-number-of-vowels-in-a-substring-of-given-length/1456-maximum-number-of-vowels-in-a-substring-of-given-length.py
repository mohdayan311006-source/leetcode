class Solution(object):
    def maxVowels(self, s, k):
        vowel=set('aeiou')
        count=0
        for ch in s[:k]:
            if ch in vowel:
                count+=1
        ans=count
        for i in range(k,len(s)):
            if s[i] in vowel:
                count+=1
            if s[i-k] in vowel:
                count-=1
            ans=max(ans,count)
        return ans
        
       

            
        

        