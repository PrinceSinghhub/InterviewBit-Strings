class Solution:
    # @param A : list of strings
    # @return a strings
    def serialize(self, A):

        ans = ""

        for i in A:
            comp = "~"
            L = len(i)
            ans+=i
            ans+=str(L)

            ans+=comp
        return ans

ans = Solution()
print(ans.serialize(['scaler', 'academy']))