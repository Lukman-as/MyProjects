class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.append(0)
        count = 1
        final = count
        for i in range(len(nums)-1):
            if 1 not in nums:
                count = 0
            
            if nums[i] == 1 and nums[i+1] == 1:
                count += 1
            elif nums[i] == 1 and nums[i+1] == 0:
                if final >= count:
                    count = 1
                else:
                    final = count
                    count = 1
                
        print(final)
           

new = Solution()
new.findMaxConsecutiveOnes([1,1,0,1,1,1])
