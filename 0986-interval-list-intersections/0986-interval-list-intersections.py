class Solution(object):
    def intervalIntersection(self, firstList, secondList):
        res=[]
        i=0
        j=0
        while i<len(firstList) and j<len(secondList):
            start1=firstList[i][0]
            end1=firstList[i][1]
            start2=secondList[j][0]
            end2=secondList[j][1]
            if start1<=start2:
                if end1>=start2:
                    res.append([max(start1,start2),min(end1,end2)])
            elif start2<=start1:
                if end2>=start1:
                    res.append([max(start1,start2),min(end1,end2)])
            if end1<=end2:
                i+=1
            else:
                j+=1
        return res
                    

        