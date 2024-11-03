class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
        mag_sorted = []
        sorted_squares = []
        for num in nums:
            if num < 0:
                mag_sorted.append(-1*num)
            else:
                mag_sorted.append(num)
        mag_sorted.sort()

        for mag in mag_sorted:
            sorted_squares.append(mag**2)


        print(sorted_squares)
            
#you dumb, use sort after squaring      
new = Solution()
new.sortedSquares([-7,-3,2,3,11])
