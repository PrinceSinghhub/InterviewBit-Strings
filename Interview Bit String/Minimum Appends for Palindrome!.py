class Solution:
    # @param A : string
    # @return an integer
    def solve(self, A):

        N = len(A) - 1
        i = 0
        j = N
        k = 0

        while i < j:
            if A[i] == A[j]:
                i += 1
                j -= 1
            else:
                k += 1
                i = k
                j = len(A) - 1
        return k
ans = Solution()
A="abede"
print(ans.solve(A))
