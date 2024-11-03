class Solution(object):
    def duplicateZeros(self, arr):
        """
        :type arr: List[int]
        :rtype: None Do not return anything, modify arr in-place instead.
        """
        zeros_to_duplicate = arr.count(0)

        length = len(arr)
        for i in range(length - 1, -1, -1):
            if i + zeros_to_duplicate < length:
                arr[i + zeros_to_duplicate] = arr[i]

            if arr[i] == 0:  # Duplicate the zero
                zeros_to_duplicate -= 1
                if i + zeros_to_duplicate < length:
                    arr[i + zeros_to_duplicate] = 0
        return arr

new = Solution()
new.duplicateZeros([1,0,2,0,3,4,5,0])