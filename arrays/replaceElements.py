class Solution(object):
    def replaceElements(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """

        maxi = -1
        for i in range(len(arr) - 1, -1, -1):
            new_max = max(maxi, arr[i])
            arr[i] = maxi
            maxi = new_max
        
        print(arr)
            
            
            

        


q = Solution()
q.replaceElements([17,18,5,4,6,1])