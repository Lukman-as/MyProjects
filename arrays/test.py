class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        unique = 1
        for check in range(1, len(nums)):
            if nums[check] != nums[check - 1]:
                nums[unique] = nums[check]
                unique += 1

        print(nums)
        

           

q = Solution()
q.removeDuplicates([1,1,2,3,3,4,5,5,6,7,7,8])