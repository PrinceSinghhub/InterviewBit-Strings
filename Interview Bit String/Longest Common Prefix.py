class Solution:
    # @param A : list of strings
    # @return a strings
    def longestCommonPrefix(self, A):

        if len(A) < 2:
            return A[0]

        A.sort()
        print(A)
        ans = ""

        l = len(A) - 1
        index = 0


        single = len(A[0])

        while index < single and A[0][index] == A[l][index]:
            ans += A[0][index]
            index += 1

        return ans



ans = Solution()
A = ["abcdefgh", "aefghijk", "abcefgh"]
print(ans.longestCommonPrefix(A))