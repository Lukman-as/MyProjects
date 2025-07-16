class Solution(object):
    def bubbleSort(self, arr):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(arr)
        for i in range(n - 1):
            swapped = False
            for j in range(n - i - 1):
                if arr[j] > arr[j + 1]:  
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]
                    swapped = True
            if not swapped: 
                break
        print(arr)
        return arr
        
        

new = Solution()
new.bubbleSort([2,3,1,5,2,3,7,2])