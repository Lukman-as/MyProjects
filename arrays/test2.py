class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """

        count = 0
        for i in range(len(nums)):
            if nums[i - count] == val:
                replace = nums.pop(i - count)
                nums.append(replace)

        return nums

new = Solution()
new.removeElement([3,2,2,3], 3)