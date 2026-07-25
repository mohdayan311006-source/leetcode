class Solution(object):
    def isValid(self, s):
        stack=[]
        pair={
            ')':'(',
            ']':'[',
            '}':'{'
        }
        for ch in s:
            if stack and ch in pair and stack[-1]==pair[ch]:
                stack.pop()
            else:
                stack.append(ch)
        if not stack:
            return True
        else:
            return False

            
        