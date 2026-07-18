class Solution(object):
    def insert(self, intervals, newInterval):
        res=[]
        app=False
        for i in range(len(intervals)):
            start=intervals[i][0]
            if app==False and start>=newInterval[0]:
                res.append(newInterval)
                app=True
            res.append([intervals[i][0],intervals[i][1]])
        if app==False:
            res.append(newInterval)
        start1=res[0][0]
        end1=res[0][1]
        new_res=[]
        for j in range(1,len(res)):
            start2=res[j][0]
            end2=res[j][1]
            if end1>=start2:
                start1=start1
                end1=max(end1,end2)
                continue
            new_res.append([start1,end1])
            start1=start2
            end1=end2
        new_res.append([start1,end1])
        return new_res

        