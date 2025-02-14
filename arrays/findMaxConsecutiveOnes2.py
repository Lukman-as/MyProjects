class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        def maxOnes(arr):
            max_count = 0
            count = 0
            for num in arr:
                if num == 1:
                    count += 1
                    max_count = max(max_count, count)
                else:
                    count = 0
            return max_count
        
        max_ones = maxOnes(nums) 
        for i in range(len(nums)):
            if nums[i] == 0:
                nums[i] = 1  
                max_ones = max(max_ones, maxOnes(nums))
                nums[i] = 0  

        return max_ones



new = Solution()
print(new.findMaxConsecutiveOnes([1, 1, 0, 0, 0, 1, 1, 1]))  


