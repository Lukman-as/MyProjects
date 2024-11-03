class Solution(object):
    def findNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        even = 0
        for num in nums:
            if len(str(num))%2 == 0:
                even += 1

        return even
                


new = Solution()
new.findNumbers([555,901,482,1771])