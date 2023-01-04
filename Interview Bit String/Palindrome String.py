class Solution:
    # @param A : string
    # @return an integer
    def isPalindrome(self, A):

        ans = ""

        for i in A:
            if i.isalnum():
                ans += i.lower()

        # print(ans)
        if ans == ans[::-1]:
            return 1
        return 0

ans = Solution()
a = "A man, a plan, a canal: Panama"
print(ans.isPalindrome(a))

