class Solution:
    # @param A : string
    # @return an integer
    def power(self, A):

        # my logic but not give write ans for n = 1
        # A = int(A)
        #
        # if A == 1:
        #     return 1
        # elif A % 2 != 0 or A == 0:
        #     return 0
        #
        # return self.power(A // 2)

        a_bin = bin(int(A))[2:]
        if sum(int(i) for i in a_bin) == 1 and a_bin[-1] != '1':
            return 1
        else: return 0
ans = Solution()
a = 1
print(ans.power(a))