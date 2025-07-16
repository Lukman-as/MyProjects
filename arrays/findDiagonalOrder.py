class Solution(object):
    def findDiagonalOrder(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: List[int]
        """
        if not mat or not mat[0]:
            return []
        
        rows, cols = len(mat), len(mat[0])
        result = []
        intermediate = []

        for d in range(rows + cols - 1):
            intermediate.clear()
            r = 0 if d < cols else d - cols + 1
            c = d if d < cols else cols - 1

            while r < rows and c > -1:
                intermediate.append(mat[r][c])
                r += 1
                c -= 1

            if d % 2 == 0:
                result.extend(intermediate[::-1])
            else:
                result.extend(intermediate)

        return result

test = Solution()
print(test.findDiagonalOrder([[1,2,3],[4,5,6],[7,8,9]]))
