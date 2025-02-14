class Solution(object):
    def validMountainArray(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """

        if len(arr) >= 3:
            j = 1
            for i in range(0, len(arr) - 1):
                if arr[i] < arr[j]:
                    j+=1
                    if j == len(arr):
                        return False
                    continue
                else:
                    if i == 0:
                        print("false")
                        return False
                    break
            
            for m in range(j, len(arr)):
                if arr[m - 1] > arr[j]:
                    j+=1
                    continue
                else:
                    print("false")
                    return False
                
            print("true")
            return True
                
new = Solution()
new.validMountainArray([1,2,3,2,3])
            
                
            




                


