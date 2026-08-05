class Solution(object):
    def removeDuplicates(self, s, k):
        stack=[]
        ans=""
        for i in range(len(s)):
            if not stack:
                stack.append((s[i],1))
                continue
            if stack[-1][0]==s[i]:
                ch,count=stack[-1]
                stack[-1]=(ch,count+1)
                if stack[-1][1]==k:
                    stack.pop()
            else:
                stack.append((s[i],1))
        for ch , count in stack:
            ans+=ch*count
        return ans
        
                

        
        