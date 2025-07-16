class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        total = sum(nums)
        temp_total = 0
        pivot = -1
        for i in range(len(nums)):
            if temp_total == (total - nums[i])/2:
                pivot = i
            temp_total += nums[i]

        return pivot

test = Solution()
test.pivotIndex([-1,-1,-1,-1,-1, -1])
