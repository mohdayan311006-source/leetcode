class Solution(object):
    def dailyTemperatures(self, temperatures):
        stack=[]
        stack.append(len(temperatures)-1)
        res=[]
        res.append(0)
        for i in range(len(temperatures)-2,-1,-1):
            while stack and temperatures[stack[-1]]<=temperatures[i]:
                stack.pop()
            if stack and temperatures[stack[-1]]>temperatures[i]:
                res.append(stack[-1]-i)
            if not stack:
                res.append(0)
            stack.append(i)
        return res[::-1]
        

        