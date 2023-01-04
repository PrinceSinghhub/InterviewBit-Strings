class Solution:
    # @param A : string
    # @return a strings
    def longestPalindrome(self, A):
        n = len(A)
        if n <= 1: return A
        start, end = 0, n
        max_len = 0
        max_substr = ""
        while start < end and max_len < n:
            for i in range(start, end):
                if A[i] == A[start] and max_len < len(A[start:i+1]):
                    mid = (start + i+1)/2.
                    if A[start:int(mid)] == A[i:int(mid-0.5):-1]:
                        max_len = len(A[start:i+1])
                        max_substr = A[start:i+1]
            start += 1
        return max_substr

ans = Solution()
A = "aaaabaaa"
print(ans.longestPalindrome(A))