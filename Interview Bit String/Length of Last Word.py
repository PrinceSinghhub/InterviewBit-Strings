class Solution:

    def lengthOfLastWord(self, A):

        if len(A) == 0:
            return 0

        ans = A.split(' ')
        for i in ans[::-1]:
            if len(i) > 0:
                return len(i)
        return 0

ans = Solution()
a = "  xDGBklKecz IAcOJYOH O  WY WPi"
print(ans.lengthOfLastWord(a))