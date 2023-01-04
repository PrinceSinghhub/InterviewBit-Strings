class Solution:
    # @param A : string
    # @return a strings
    def solve(self, A):

        ans = ""
        for i in A:
            if i not in ans:
                count = A.count(i)
                ans += i
                ans += str(count)

        return ans

ans = Solution()
print(ans.solve("abbhuabcfghh"))