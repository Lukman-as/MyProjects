class Solution(object):
    def checkIfExist(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """

        j = len(arr)
        for i in range(j):
            for m in range(j):
                if arr[i] == 2*arr[m] and i != m:
                    print("x")
                    return True
        

        return False

new = Solution()
new.checkIfExist([-2,0,10,-19,4,6,-8])
            
