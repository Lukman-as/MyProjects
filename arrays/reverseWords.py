class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """

        return ' '.join(word[::-1] for word in s.split(" "))

        


        
        
        



new = Solution()
new.reverseWords("Hi my name is Lukman")