# Definition for singly-linked list.



class Solution(object):
    def mergeTwoLists(self, nums1,m, n,  nums2):
        for i in range(len(nums1) - 1, m - 1, -1):
            nums1[i] = nums2[n - 1]
            n -= 1
                   
        nums1.sort()
        print(nums1)
    

q = Solution()
q.mergeTwoLists([1,2,3,0,0,0],3, 3, [2,5,6])
