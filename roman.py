class Solution(object):
    def romanToInt(self, s):
        roman = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        answer = 0
        for i in range(len(s) - 1):
            # print(roman[i])
            print(s[i])
            print(roman[s[i]])
            if roman[s[i]] < roman[s[i+1]]:
                answer -= roman[s[i]]
            else:
                answer += roman[s[i]]
        return answer + roman[s[-1]]
    
def main():
    p1 = Solution()
    s = input("Enter a roman number: ")
    num = p1.romanToInt(s)
    print(num)
    return

main()