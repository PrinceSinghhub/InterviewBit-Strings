class Solution:
    # @param A : string
    # @return an integer
    def solve(self, A):
        if len(A) < 2:
            return 0
        vow = 'aeiou'
        v = 0
        for i in vow:
            v += A.count(i)

        return v * (len(A) - v) % (10 ** 9 + 7)

ans = Solution()
A = "aba"
print(ans.solve(A))