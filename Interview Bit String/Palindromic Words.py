class Solution:
    # @param A : string
    # @return an integer
    def solve(self, A):


        A = A.split(" ")
        # print(A)

        ans = [1 for i in A if i == i[::-1]]
        # print(ans)
        return len(ans)

ans = Solution()
print(ans.solve("the fastest racecar"))