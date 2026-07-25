class Solution(object):
    def isValid(self, s):
        stack=[]
        for i in range(len(s)):
            if stack and s[i]==')' and stack[-1]=='(':
                stack.pop()
            elif stack and s[i]==']' and stack[-1]=='[':
                stack.pop()
            elif stack and s[i]=='}' and stack[-1]=='{':
                stack.pop()
            else:
                stack.append(s[i])
        if not stack:
            return True
        else:
            return False

            
        