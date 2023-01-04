class Solution:
    # @param A : string
    # @return a list of integers
    def solve(self, A):

        arr = list(set(A))
        ans = []
        for i in A:
            if i in arr:
                ans.append(A.count(i))
                arr.remove(i)

        return ans

ans = Solution()
s = "interviewbit"
print(ans.solve(s))