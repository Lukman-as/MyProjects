class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        arr = list(set(nums))
        nums[:len(arr)] = arr
        return len(arr), nums
        

        
        
        
            

            

            

        

q = Solution()
q.removeDuplicates([1,1,2])