class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        value = 0

        for i in range(len(digits)):
            value += digits[i]*10**(len(digits) - i - 1)

        value += 1
        list2 = list(map(int, str(value)))
        return list2
        

test = Solution()
test.plusOne([1,2,3])


