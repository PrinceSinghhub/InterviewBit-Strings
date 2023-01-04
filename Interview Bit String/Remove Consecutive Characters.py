class Solution:
    # @param A : string
    # @param B : integer
    # @return a strings
    def solve(self, A, B):
        s=''
        i=0
        while i<len(A):
            if A[i:i+B]==A[i]*B:
                i=i+B
                continue
            s=s+A[i]
            i=i+1
        return s

ans = Solution()
A = "aabcd"
B = 2

print(ans.solve(A,B))
