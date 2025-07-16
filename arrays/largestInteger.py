class Solution(object):
    def dominantIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        max = 0
        for i in range(len(nums)):
            if nums[i] >= max:
                max = nums[i]
                max_index = i

        
        for num in nums:
            if num > max/2 and num != max:
                return -1

        return max_index
                
            


test = Solution()
test.dominantIndex([2,1,7,3])
