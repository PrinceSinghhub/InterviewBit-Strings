class Solution:

    def addBinary(self, A, B):

        ans = bin(int(A,2) + int(B,2))[2::]
        return ans

ans = Solution()
a = "100"
b = "11"
print(ans.addBinary(a,b))
