class Solution:
    # @param A : string
    # @return a strings
    def solve(self, A):

        ans = ""

        for i in A:
            if i.islower():
                ans+=i.upper()
            else:
                ans+=i.lower()
        return ans

ans = Solution()
print(ans.solve("InterviewBit"))