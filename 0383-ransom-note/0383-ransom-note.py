class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        have={}
        req={}
        for ch in magazine:
            have[ch]=have.get(ch,0)+1
        for ch in ransomNote:
            req[ch]=req.get(ch,0)+1
        for ch in req:
            if have.get(ch,0)<req[ch]:
                return False 
        return True
        
        
        
            