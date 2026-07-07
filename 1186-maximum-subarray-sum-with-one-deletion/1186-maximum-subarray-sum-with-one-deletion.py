class Solution(object):
    def maximumSum(self, arr):
        nodelet=arr[0]
        res=arr[0]
        onedelet=float('-inf')
        for i in range(1,len(arr)):
            preNodelet=nodelet
            nodelet=max(nodelet+arr[i],arr[i])
            onedelet=max(preNodelet,onedelet+arr[i])
            res=max(res,nodelet,onedelet)
        return res

       
        