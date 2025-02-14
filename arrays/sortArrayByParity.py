class Solution(object):
    def sortArrayByParity(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        odd_count = 0
        for count in range(len(nums)):
            if nums[count - odd_count]%2 != 0:
                odd = nums.pop(count - odd_count)
                nums.append(odd)
                odd_count += 1
                
        return nums


q = Solution()
q.sortArrayByParity([3,1,2,4])