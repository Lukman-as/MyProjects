class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """

        swap_count = 0

        for count in range(len(nums)):
            print(count - swap_count)
            if nums[count - swap_count] == 0:
                nums.pop(count - swap_count)
                nums.append(0)
                swap_count += 1
        
        
        print(nums)

        
        


q = Solution()
q.moveZeroes([17,18,0,0,0,1])
            
                    

